#This program attempts to create a graphing calculator using the library matplotlib.

import matplotlib.pyplot as graph
import math

#setting up variables and lists to store data

#Variables
a,b,c,d,n,x,y,t = 0,0,0,0,0,0,0,0
t_2 = (2*math.pi)
graph_extension, sine, cosine, graph_counter = 0,0,0,0
precision = 1000 #Manual precision change (default: 100)

#List pairs / Check if this is needed Perhaps only the final_x and final_y should be here
x_val, y_val = [],[]
x_val2, y_val2 = [],[]
x_val3, y_val3 = [],[]
final_x, final_y = [],[]
poly_c, poly_d = [],[]
poly_c2, poly_d2 = [],[]

repeat = 1 # Control variable for while loop

# -----------------------------FUNCTIONS-------------------------------

def my_root (base, n):
    if n % 2 == 0:
        result = base**(1/n)
    else:
        if base >= 0:
            result = base**(1/n)
        else:
            base = -base
            result = -(base**(1/n))
    return result


while(repeat == 1):

    repeat, switch = 3,0
    asymptote,  asymptote2 = 0,0
    x,t,y,y1,y2 = 0,0,0,0,0
    x_val, y_val =  [],[]
    x_val2, y_val2 = [],[]
    x_val3, y_val3 = [],[]
    poly_c, poly_d = [],[]
    poly_c2, poly_d2 = [],[]
    
    # User interface/ Getting input

    print("\nWelcome to the graphing calculator!\n")
    print("From the list imput the number corresponding to the desired function type\n")
    print("1) Plynomial       2) Squared root       3) Cubic root\n"
          "4) Cardioid        5) Spiral             6) Lemniscate\n"
          "7) Roses           8) Logarithm          9) Exponential\n"
          "10) Rational      11) Sine              12) Cosine\n"
          "13) Tangent       14) Exit")
    user_choice = int(input("\nPlease input your choice: "))

    if user_choice == 1 or user_choice == 2 or user_choice == 3 or user_choice == 8 or user_choice == 9 or user_choice == 10:
        
        number_of_points = int (input("Please enter the number of points to plot (even quantity): "))

    elif user_choice != 14: #change to an 'elif'. If user inputs any number, the program displays the input unnecessarily
        max_angle = int (input("Please enter the maximum angle desired for the graph (in degrees): "))

    # Identifying the type of graph desired

    if user_choice == 2:

        graph_label = 'Squared root'
        print("Function in the form: y = a*x^1/2 + c")
        a = float(input("Input the 'a' coefficient: "))
        c = float(input("Input the y-shift: "))

        for i in range (0, (number_of_points * precision)+1):

            y = a*x**0.5 + c # Equation for the squared root

            x_val.append(x)
            y_val.append(y)

            x += (1/precision)
        
    elif user_choice == 3:

        graph_label = 'Cubic root'
        print("Function in the form: y = a*x^1/3 + c")
        a = float(input("Input the 'a' coefficient: "))
        c = float(input("Input the y-shift: "))
        x = -(number_of_points/2)
        
        for i in range (0, (number_of_points * precision)+1):
            
            y = a*my_root(x, 3)+c # Equation for the cubic root

            x_val.append(x)
            y_val.append(y)

            x += (1/precision)

    elif user_choice == 1:
        
        graph_label = 'Polynomial'
        print("Function in the form: y = an*x^n + a(n-1)*x^(n-1)+ ... + a2*x^2 + a1*x + a0")
        degree = int(input("Enter the maximum degree of the polynomial: "))
        x = -number_of_points/2
        
        for i in range (0, (degree+1)):
            poly_c.append(float(input("Enter the coefficients from right to left: ")))
            poly_d.append(i)

        for i in range (0, (number_of_points * precision)+1):
            for j in range (0, (degree+1)):
                y += poly_c[j]*x**poly_d[j]
                
            x_val.append(x)
            y_val.append(y)

            x += (1/precision)   
            y = 0
        
    elif user_choice == 4:

        graph_label = 'Cardioid'
        print("Function in the form: r = a + b*(sin(t)/cos(t))")
        a = float(input("Input the 'a' number of the polar equation: "))
        b = float(input("Input the 'b' coefficient of the polar equation: "))
        trig_function = input("Is it the 'sine' or the 'cosine'? (Input the name of the corresponding trigonometric function): ")
        
        if trig_function == 'sine':

            for i in range (0, (max_angle*precision)):

                r = a + b*math.sin(t) # Cardioid equation (sine)

                x = r*math.cos(t) # Conversion from Polar to Cartesian
                y = r*math.sin(t) #-^
                
                t += ((math.pi/180)/precision) # Update rate(~1 degree in radians)
                
                x_val.append(x)
                y_val.append(y)

        elif trig_function == 'cosine':

            for i in range (0, (max_angle*precision)):
                
                r = a + b*math.cos(t) # Cardioid equation (cosine)

                x = r*math.cos(t)
                y = r*math.sin(t)
                
                t += ((math.pi/180)/precision)

                x_val.append(x)
                y_val.append(y)
                
        else:
             print("Error, trigonometric function not recognized or available.")

    elif user_choice == 5:

        graph_label = 'Spiral'
        print("Function in the form: r = a*t^n")
        a = float(input("Input numerical coefficient 'a': "))
        degree = float(input("Input the degree of the angle: "))
        
        for i in range (0, max_angle*precision):

            r = a*t**degree # Spiral equation

            x = r*math.cos(t)
            y = r*math.sin(t)

            t += ((math.pi/180)/precision) # Update rate(~1 degree in radians)

            x_val.append(x)
            y_val.append(y)
            
    elif user_choice == 6:
        
        graph_label = 'Lemniscate'
        print("Function in the form: r = (a*(sin(t)/cos(t)))^1/2")
        a = float(input("Enter the 'a' coefficient: "))
        n = int(input("Enter the coefficient of the angle: "))
        trig_function = input("Is it 'sine' or the 'cosine'?"
                              "(Input the name of the corresponding trigonometric function): ")
       
        if trig_function == 'sine':
            
            for i in range (0, (max_angle*precision)):

                r = (a*math.sin(n*t))**0.5 # Lemniscate equation (sine)

                x = r*math.cos(t)
                y = r*math.sin(t)

                if a*math.sin(n*t) > 0:
                    x_val.append(x)
                    y_val.append(y)
                if i == 0:
                    x_val.append(0)
                    y_val.append(0) 
                                    
                t += ((math.pi/180)/precision) # Update rate(~1 degree in radians)

        elif trig_function == 'cosine': 
            
            for i in range (0, (max_angle*precision)):
                
                r = (a*math.cos(n*t))**0.5 # Lemniscate equation (cosine)
                
                x = r*math.cos(t)
                y = r*math.sin(t)

                if a*math.cos(n*t) > 0:
                    x_val.append(x)
                    y_val.append(y)
                
                t += ((math.pi/180)/precision) # Update rate(~1 degree in radians)

    elif user_choice == 7:

        graph_label = 'Roses'
        print("Function in the form: r = a*(sin(n*t)/cos(n*t))")
        a = float(input("Input the 'a' coefficient: "))
        n = int(input("Input the 'n' coefficient for the angle: "))
        trig_function = input("Is it 'sine' or the 'cosine'? (Input the name of the corresponding trigonometric function): ")
        
        if trig_function == 'sine':
            
            for i in range (0, (max_angle*precision)):

                r = a*math.sin(n*t) # Roses equation (sine)
                
                x = r*math.cos(t)
                y = r*math.sin(t)
                
                x_val.append(x)
                y_val.append(y)            

                t += ((math.pi/180)/precision) # Update rate (depends on 'precision')
                
        elif trig_function == 'cosine': 

            for i in range (0, (max_angle*precision)):
                
                r = a*math.cos(n*t) # Roses equation (cosine)
                
                x = r*math.cos(t)
                y = r*math.sin(t)
                
                x_val.append(x)
                y_val.append(y)            

                t += ((math.pi/180)/precision)# Update rate (depends on 'precision')
            
        else:
             print("Error, trigonometric function not recognized or available.")

    elif user_choice == 8:

        graph_label = 'Logarithm'
        print("Function in the form: a*log base(x)")
        a = float(input("Input the 'a' coefficient: "))
        base = float(input("Input the 'base' for the logarithm: "))
        x = 1/(precision)**3
        
        for i in range (0, (number_of_points * precision)+1):

            y = a*math.log(x,base)

            y_val.append(y)
            x_val.append(x)

            x += (1/precision)
            
    elif user_choice == 9:

        graph_label = 'Exponential'
        print("Function in the form: a*(base)^x")
        a = float(input("Input the 'a' coefficient: "))
        base = float(input("Input the 'base' for the logarithm: "))
        x = -number_of_points/2

        for i in range (0, (number_of_points * precision)+1):

            y = a*(base)**x

            y_val.append(y)
            x_val.append(x)

            x += (1/precision)
##--------------------------------CONSTRUCTION IN PLACE, CAUTION! ;) ---------------------------------
##    elif user_choice == 10:
##
##        graph_label = 'Rational' #FIX: Fix this print for function form
##        print("Function in the form:     an*x^n + a(n-1)*x^(n-1)+ ... + a2*x^2 + a1*x + a0\n"
##              "                     y =  _________________________________________________\n"
##              "                          an*x^n + a(n-1)*x^(n-1)+ ... + a2*x^2 + a1*x + a0\n")
##        
##        l_dom = float(input("Input the smaller number of the domain: "))
##        h_dom = float(input("Input the greatest number of the domain: "))
##        #Ask also for range to set boundaries for the graph because it's infinite
##        degree = int(input("Enter the greatest degree of the nominator: "))
##        degree2 = int(input("Enter the greatest degree of the denominator: "))
##
##        domain_size = int(math.fabs(l_dom) + math.fabs(h_dom))
##        x = l_dom
##        graph_jump = 0
##        
##        for i in range (0, (degree+1)):
##            poly_c.append(float(input("Enter the coefficients from right to left (nominator): ")))
##            poly_d.append(i)
##            
##        for i in range (0, (degree2+1)):
##            poly_c2.append(float(input("Enter the coefficients from right to left(denominator): ")))
##            poly_d2.append(i)
##
##        #print(*poly_c)
##        #print(*poly_c2)
##        #print(*poly_d)
##        #print(*poly_d2)
##        #FIX: Not graphing all values stored on the lists
##        #FIX: Apparently graph_jump is not working properly
##        #FIX: Find Assymptotes
##        for i in range (0, (domain_size*precision)+1):
##            
##            for j in range (0, (degree2+1)):   
##                y2 += poly_c2[j]*x**poly_d2[j]
##                
##            #print(y2)
##            # Recognizing the functions's asymptotes
##            if math.fabs(y2) < (1/precision**2) and switch == 0:
##                asymptote = x #remember that there might be more than one asymptote
##                switch = 1
##                print("***The asymptote is: ", asymptote)
##            elif math.fabs(y2) < (1/precision**2) and switch == 1:
##                asymptote2 = x
##                print("***The asymptote # 2 is: ", asymptote2)
##                
##            y2 = 0
##            x += (1/precision)
##            
##        x = l_dom
##         
##------------------------------------------------------------------------------------------     
##        for i in range (0, (domain_size*precision)+1):
##            
##            for j in range (0, (degree+1)):
##                y1 += poly_c[j]*x**poly_d[j]
##
##            for j in range (0, (degree2+1)):   
##                y2 += poly_c2[j]*x**poly_d2[j]
##                
##            #print(y,"      ",x)
##            y = y1/y2 #FIX: Zero division error, check y2
##
##            # Trigger to recognize when to separate different sections of the graph
##            if x >= asymptote or x>= asymptote2:
##                if x >= asymptote and x<= asymptote2:
##                    graph_jump = 1
##                    x += (1/precision)
##                elif x >= asymptote2:
##                    graph_jump = 2
##                    x += (1/precision)
##                
##            if graph_jump == 0:
##                y_val.append(y)
##                x_val.append(x)
##                
##            elif graph_jump == 1:
##                if y > 0: #FIX: Why is the y negative still in 1/x?
##                    y_val2.append(y)
##                    x_val2.append(x)
##
##            elif graph_jump == 2:
##                y_val3.append(y)
##                y_val3.append(x)
##
##            y1, y2 = 0,0
##            x += (1/precision)
##            #print("***Graph Jum", graph_jump)
##    #...
##---------------------------------END OF CONSTRUCTION ZONE--------------------------------------
            
    elif user_choice == 11:
        graph_label = 'Sine'

        print("Function of the form: a*sin(c*(t-b))+d")

        a = float(input("Input the 'a' coefficient: "))
        b = float(input("Input the 'b' coefficient: "))
        c = float(input("Input the 'c' coefficient: "))
        d = float(input("Input the 'd' coefficient: "))

        for i in range (0, (max_angle*precision)):

            y = a*math.sin(c*(t-b))+d

            x_val.append(t)
            y_val.append(y)

            t += ((math.pi/180)/precision)

    elif user_choice == 12:
        graph_label = 'Cosine'

        print("Function of the form: a*cos(c*(t-b))+d")

        a = float(input("Input the 'a' coefficient: "))
        b = float(input("Input the 'b' coefficient: "))
        c = float(input("Input the 'c' coefficient: "))
        d = float(input("Input the 'd' coefficient: "))

        for i in range (0, (max_angle*precision)):

            y = a*math.cos(c*(t-b))+d

            x_val.append(t)
            y_val.append(y)

            t += ((math.pi/180)/precision)
            
    elif user_choice == 13:
        print("\nSorry Option not yet available.\n"
              "It is needed an algorithm to set the Asymptotes first\n"
              "Without it I cannot make an accurate graph that follows\n"
              "Such a smooth path towards infinity. Iprovement needed!\n")
        
    elif user_choice == 14:
        graph_label = 'Close this plotting window to exit...Bye!'
        repeat = 0
        
        
    #----------------------------------PLOTTING (MATPLOTLIB)--------------------------------

    # Testing checks
    
    #print(*x_val)
    #print(*y_val)
    #print(*x_val2)
    #print(*y_val2)
    #print(graph_counter)

    final_x.append(x_val)
    final_y.append(y_val)
    
    if user_choice == 6: # Only for Cubic root function
        final_x.append(x_val3)
        final_y.append(y_val3)
        graph_counter += 1
        
    if user_choice == 10:
        
        if graph_jump == 1:
            final_x.append(x_val2)
            final_y.append(y_val2)
            graph_counter += 1
            
        elif graph_jump == 2:
            final_x.append(x_val2)
            final_y.append(y_val2)
            final_x.append(x_val3)
            final_y.append(y_val3)
            graph_counter += 2            
    
    # plotting values on the graph
            
    for k in range (0, (graph_counter+1)): 
        graph.plot(final_x[k], final_y[k])# Graph mother graph(s)
        
        # Testing checks
        
        #print(k)
        #print(*final_x[k])
        #print(*final_y[k])

    # labeling and formatting axis and axes
    graph.xlabel('x-axis')
    graph.ylabel('y-axis')
    if (graph_counter == 0):
        graph.title(graph_label)
    else:
        graph.title('Multiple graphs')
    
    graph.grid(color='k', linestyle='-', linewidth=0.20)

    # Determining and setting axis limits; this may be used for zooming in when
    # calculating areas for especific regions.
    
##    if graph_counter == 0:
##        x_min = min(x_val)
##        x_max = max(x_val)
##        y_min = min(y_val)
##        y_max = max(y_val)
##    else:
##        if min(x_val) < x_min:
##            x_min = min(x_val)
##        if max(x_val) > x_max:
##            x_max = max(x_val)
##        if min(y_val) < y_min:
##            y_min = min(y_val)
##        if max(y_val) > y_max:
##            y_max = max(y_val)    
##    graph.axis([x_min,x_max,y_min,y_max]) 

    # Showing the graph
    
    graph.show()
    
    while(repeat != 1 and repeat != 0):
        repeat = int(input("To sketch multiple graphs enter '1', to exit enter '0': "))
        
    graph_counter += 1
    
print("BYE!")
