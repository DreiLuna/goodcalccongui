from tkinter import *
import tkinter.font as tkFont

global ddc
ddc = 0
global user_num1
user_num1= 0

def ex0(ddc, user_num1):
    ddc = ddc + 1

    

    if ddc != 2:
        user_num1 = 0
    elif ddc == 2:
        user_num1_ram = user_num1 * 10

        user_num1_ram = user_num1_ram + 1
        print (user_num1_ram)
        
def ex1(ddc, user_num1):
    ddc = ddc + 1

    

    if ddc != 2:
        user_num1 = 1
    elif ddc == 2:
        user_num1_ram = user_num1 * 10

        user_num1_ram = user_num1_ram + 1
        print (user_num1_ram)
        
def ex2(ddc, user_num1):
    ddc = ddc + 1

    
    if ddc != 2:
        user_num1 = 2
    elif ddc == 2:
        user_num1_ram = user_num1 * 10

        user_num1_ram = user_num1_ram + 1
        print (user_num1_ram)
        
def ex3(ddc, user_num1):
    ddc = ddc + 1

    
    if ddc != 2:
        user_num1 = 3
    elif ddc == 2:
        user_num1_ram = user_num1 * 10

        user_num1_ram = user_num1_ram + 1
        print (user_num1_ram)
        
def ex4(ddc, user_num1):
    ddc = ddc + 1

    if ddc != 2:
        user_num1 = 4
    elif ddc == 2:
        user_num1_ram = user_num1 * 10

        user_num1_ram = user_num1_ram + 1
        print (user_num1_ram)
        
def ex5(ddc, user_num1):
    ddc = ddc + 1

    
    if ddc != 2:
        user_num1 = 5
    elif ddc == 2:
        user_num1_ram = user_num1 * 10

        user_num1_ram = user_num1_ram + 1
        print (user_num1_ram)
        
def ex6(ddc, user_num1):
    ddc = ddc + 1

    

    if ddc != 2:
        user_num1 = 6
    elif ddc == 2:
        user_num1_ram = user_num1 * 10

        user_num1_ram = user_num1_ram + 1
        print (user_num1_ram)
        
def ex7(ddc, user_num1):
    ddc = ddc + 1

    
    if ddc != 2:
        user_num1 = 7
    elif ddc == 2:
        user_num1_ram = user_num1 * 10

        user_num1_ram = user_num1_ram + 1
        print (user_num1_ram)
        
def ex8(ddc, user_num1):
    ddc = ddc + 1

    
    if ddc != 2:
        user_num1 = 8
    elif ddc == 2:
        user_num1_ram = user_num1 * 10

        user_num1_ram = user_num1_ram + 1
        print (user_num1_ram)
        
def ex9(ddc, user_num1):
    ddc = ddc + 1

    
    if ddc != 2:
        user_num1 = 9
    elif ddc == 2:
        user_num1_ram = user_num1 * 10

        user_num1_ram = user_num1_ram + 1
        print (user_num1_ram)
        
height=3
width=5
root = Tk()

root.geometry('300x300')

num1 = Button(root, text="1", height=height, width=width, command = ex1(ddc, user_num1))
num2 = Button(root, text="2", height=height, width=width, command = ex2(ddc, user_num1))
num3 = Button(root, text="3", height=height, width=width, command = ex3(ddc, user_num1))
num4 = Button(root, text="4", height=height, width=width, command = ex4(ddc, user_num1))
num5 = Button(root, text="5", height=height, width=width, command = ex5(ddc, user_num1))
num6 = Button(root, text="6", height=height, width=width, command = ex6(ddc, user_num1))
num7 = Button(root, text="7", height=height, width=width, command = ex7(ddc, user_num1))
num8 = Button(root, text="8", height=height, width=width, command = ex8(ddc, user_num1))
num9 = Button(root, text="9", height=height, width=width, command = ex9(ddc, user_num1))
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