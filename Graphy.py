# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 17:47:37 2020

@author: Eriel
"""
from tkinter import *
from matplotlib import *
from PIL import Image, ImageTk


def menu():
    # Menu Window
    menu = Tk() 
    menu.geometry('500x500') 
    menu.title("Menu")
    menu.iconbitmap(r'graphy.ico')
    menu['bg'] = '#161616'
    
    # Image Header
    canvas = Canvas(menu, height = 244, width = 365, bg = '#161616' )
    canvas.pack(pady= 20)
    wel_img = PhotoImage(file='...\src\img\welcome.png')
    canvas.create_image(0, 0, anchor = NW,  image = wel_img)
    
    # Selection Frame
    btn_frame = Frame(menu, bg = '#161616')
    btn_frame.pack()
    graph_btn = PhotoImage(file = r"graph_btn.png")
    exit_btn = PhotoImage(file = r"exit_btn.png")
    btn = Button(btn_frame, image = graph_btn, command = graphy, bg = '#161616')
    btn.pack(pady = 10)
    btn = Button(btn_frame, image = exit_btn, bg = '#161616')
    btn.pack(pady = 10)
    
    menu.mainloop() # Runs menu in a loop

def graphy():
    # Graphy Window
    graph = Tk() 
    graph.geometry('1500x500') 
    graph.title("Graphy")
    graph.iconbitmap(r'graphy.ico')
    graph['bg'] = '#161616'
    
    def change(*args):
        print("running change")
    
    OPTIONS = [
        "Linear",
        "Squared",
        "Cubic",
        "Squared root",
        "Cubic root",
        "Cardioid",
        "Lemniscate",
        "Spiral",
        "Roses"
        ]
    
    var = StringVar(graph)
    var.set("Select One")
    var.trace("w", change)
    
    down_menu = OptionMenu(graph, var, OPTIONS[0], OPTIONS[1], OPTIONS[2])
    down_menu.pack()

menu()