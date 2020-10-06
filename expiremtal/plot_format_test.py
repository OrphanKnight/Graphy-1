# -*- coding: utf-8 -*-
"""
Created on Mon May  4 12:54:52 2020

@author: Eriel
"""


import matplotlib.pyplot as plt

o = [1,2,3,4]
o1 = [1,2,3,4]
o2 = [2,3,4,5]
o3 = [3,6,9,15]
x3 = [1,2,3,4]

x=[o, o, o, o, o]
y=[o1, o2,[3,4,5,6],[7,8,9,10], [5,7,9,11]]
colours=['r','g','b','k','m-.','g-h','b-h','k-h']
plt.figure() # In this example, all the plots will be in one figure.    

x.append(x3)
y.append(o3)

for i in range(len(x)):
    plt.plot(x[i],y[i],colours[i])
plt.show()

plt.plot(x[1], y[1], colours[1])
plt.show()