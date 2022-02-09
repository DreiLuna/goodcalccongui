from tkinter import *
import tkinter.font as tkFont

def test():
    print("it worked")
def ex1():
    print("1")
def ex2():
    print("2")
def ex3():
    print("3")
def ex4():
    print("4")
def ex5():
    print("5")
def ex6():
    print("6")
def ex7():
    print("7")
def ex8():
    print("8")
def ex9():
    print("9")
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

num1.place(x=100, y=100)
num2.place(x=150, y=100)
num3.place(x=200, y=100)
num4.place(x=100, y=150)
num5.place(x=150, y=150)
num6.place(x=200, y=150)
num7.place(x=100, y=200)
num8.place(x=150, y=200)
num9.place(x=200, y=200)

root.mainloop()