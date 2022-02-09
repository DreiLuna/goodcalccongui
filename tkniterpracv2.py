from tkinter import *
import tkinter.font as tkFont

global ddc
ddc = 0
global user_num1
user_num1= 0

def ex0():
    global ddc
    global user_num1
    if ddc != 2:
        ddc = ddc + 1

    

    if ddc != 2:
        
        user_num1 = 0
        print(user_num1)
    elif ddc == 2:
        user_num1 = user_num1 * 10

        user_num1 = user_num1 + 0
        print (user_num1)
        
def ex1():
    global ddc
    global user_num1
    if ddc != 2:
        ddc = ddc + 1

    

    if ddc != 2:
        user_num1 = 1
        print(user_num1)
    elif ddc == 2:
        user_num1 = user_num1 * 10

        user_num1 = user_num1 + 1
        print (user_num1)
        
def ex2():
    global ddc
    global user_num1
    if ddc != 2:
        ddc = ddc + 1

    
    if ddc != 2:
        user_num1 = 2
        print(user_num1)
    elif ddc == 2:
        user_num1 = user_num1 * 10

        user_num1 = user_num1 + 2
        print (user_num1)
        
def ex3():
    global ddc
    global user_num1
    if ddc != 2:
        ddc = ddc + 1

    
    if ddc != 2:
        user_num1 = 3
        print(user_num1)
    elif ddc == 2:
        user_num1 = user_num1 * 10

        user_num1 = user_num1 + 3
        print (user_num1)
        
def ex4():
    global ddc
    global user_num1
    if ddc != 2:
        ddc = ddc + 1

    if ddc != 2:
        user_num1 = 4
        print(user_num1)
    elif ddc == 2:
        user_num1 = user_num1 * 10

        user_num1 = user_num1 + 4
        print (user_num1)
        
def ex5():
    global ddc
    global user_num1
    if ddc != 2:
        ddc = ddc + 1

    
    if ddc != 2:
        user_num1 = 5
        print(user_num1)
    elif ddc == 2:
        user_num1 = user_num1 * 10

        user_num1 = user_num1 + 5
        print (user_num1)
        
def ex6():
    global ddc
    global user_num1
    if ddc != 2:
        ddc = ddc + 1

    

    if ddc != 2:
        user_num1 = 6
        print(user_num1)
    elif ddc == 2:
        user_num1 = user_num1 * 10

        user_num1 = user_num1 + 6
        print (user_num1)
        
def ex7():
    global ddc
    global user_num1
    if ddc != 2:
        ddc = ddc + 1

    
    if ddc != 2:
        user_num1 = 7
        print(user_num1)
    elif ddc == 2:
        user_num1 = user_num1 * 10

        user_num1 = user_num1 + 7
        print (user_num1)
        
def ex8():
    global ddc
    global user_num1
    if ddc != 2:
        ddc = ddc + 1

    
    if ddc != 2:
        user_num1 = 8
        print(user_num1)
    elif ddc == 2:
        user_num1 = user_num1 * 10

        user_num1 = user_num1 + 8
        print (user_num1)
        
def ex9():
    global ddc
    global user_num1
    if ddc != 2:
    
        ddc = ddc + 1

    
    if ddc != 2:
        user_num1 = 9
        print(user_num1)
    elif ddc == 2:
        user_num1 = user_num1 * 10

        user_num1 = user_num1 + 9
        print (user_num1)
        





height=3
width=5
root = Tk()

root.geometry('300x300')

num1 = Button(root, text="1", height=height, width=width, command = ex1)
num2 = Button(root, text="2", height=height, width=width, command = ex2)
num3 = Button(root, text="3", height=height, width=width, command = ex3)
num4 = Button(root, text="4", height=height, width=width, command = ex4)
num5 = Button(root, text="5", height=height, width=width, command = ex5)
num6 = Button(root, text="6", height=height, width=width, command = ex6)
num7 = Button(root, text="7", height=height, width=width, command = ex7)
num8 = Button(root, text="8", height=height, width=width, command = ex8)
num9 = Button(root, text="9", height=height, width=width, command = ex9)
num0 = Button(root, text="0", height=3, width=12, command = ex0)

num1.place(x=100, y=100)
num2.place(x=150, y=100)
num3.place(x=200, y=100)
num4.place(x=100, y=150)
num5.place(x=150, y=150)
num6.place(x=200, y=150)
num7.place(x=100, y=200)
num8.place(x=150, y=200)
num9.place(x=200, y=200)
num0.place(x=100, y=260)

root.mainloop()