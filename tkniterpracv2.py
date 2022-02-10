from doctest import Example
from math import expm1
from tkinter import *
import tkinter.font as tkFont

global answer
answer = 0
global opl
opl = "+"
global ddc
ddc = 0
global ddc2
ddc2 = 0
global user_num1
user_num1= 0
global user_num2
user_num2 = 0
global second_num
second_num = 0
#! 0
def ex0():
    global ddc
    global ddc2
    global user_num1
    global user_num2
    if second_num != 1:
        if ddc != 2:
            ddc = ddc + 1

        

        if ddc != 2:
            user_num1 = 1
            print(user_num1)
            changetext()
        elif ddc == 2:
            user_num1 = user_num1 * 10

            user_num1 = user_num1 + 0
            print (user_num1)
            changetext()
    elif second_num == 1:
        if ddc2 != 2:
            ddc2 = ddc2 + 0

        

        if ddc2 != 2:
            user_num2 = 0
            print(user_num2)
            changetext()
        elif ddc2 == 2:
            user_num2 = user_num2 * 10

            user_num2 = user_num2 + 0
            print (user_num2)
            changetext()

#! 1
def ex1():
    global ddc
    global ddc2
    global user_num1
    global user_num2
    if second_num != 1:
        if ddc != 2:
            ddc = ddc + 1

        

        if ddc != 2:
            user_num1 = 1
            print(user_num1)
            changetext()
        elif ddc == 2:
            user_num1 = user_num1 * 10

            user_num1 = user_num1 + 1
            print (user_num1)
            changetext()
    elif second_num == 1:
        if ddc2 != 2:
            ddc2 = ddc2 + 1

        

        if ddc2 != 2:
                user_num2 = 1
                print(user_num2)
                changetext()
        elif ddc2 == 2:
            user_num2 = user_num2 * 10

            user_num2 = user_num2 + 1
            print (user_num2)
            changetext()

#!2
def ex2():
    global ddc
    global ddc2
    global user_num1
    global user_num2
    if second_num != 1:
        if ddc != 2:
            ddc = ddc + 1

        

        if ddc != 2:
            user_num1 = 2
            print(user_num1)
            changetext()
        elif ddc == 2:
            user_num1 = user_num1 * 10

            user_num1 = user_num1 + 2
            print (user_num1)
            changetext()
    elif second_num == 1:
        if ddc2 != 2:
            ddc2 = ddc2 + 1

        

        if ddc2 != 2:
            user_num2 = 2
            print(user_num2)
            changetext()
        elif ddc2 == 2:
            user_num2 = user_num2 * 10

            user_num2 = user_num2 + 2
            print (user_num2)
            changetext()
#!3
def ex3():
    global ddc
    global ddc2
    global user_num1
    global user_num2
    if second_num != 1:
        if ddc != 2:
            ddc = ddc + 1

        

        if ddc != 2:
            user_num1 = 3
            print(user_num1)
            changetext()
        elif ddc == 2:
            user_num1 = user_num1 * 10

            user_num1 = user_num1 + 3
            print (user_num1)
            changetext()
    elif second_num == 1:
        if ddc2 != 2:
            ddc2 = ddc2 + 1

        

        if ddc2 != 2:
            user_num2 = 3
            print(user_num2)
            changetext()
        elif ddc2 == 2:
            user_num2 = user_num2 * 10

            user_num2 = user_num2 + 3
            print (user_num2)
            changetext()

#! 4
def ex4():
    global ddc
    global ddc2
    global user_num1
    global user_num2
    if second_num != 1:
        if ddc != 2:
            ddc = ddc + 1

        

        if ddc != 2:
            user_num1 = 4
            print(user_num1)
            changetext()
        elif ddc == 2:
            user_num1 = user_num1 * 10

            user_num1 = user_num1 + 4
            print (user_num2)
            changetext()
    elif second_num == 1:
        if ddc2 != 2:
            ddc2 = ddc2 + 1

        

        if ddc2 != 2:
            user_num2 = 4
            print(user_num2)
            changetext()
        elif ddc2 == 2:
            user_num2 = user_num2 * 10

            user_num2 = user_num2 + 4
            print (user_num2)
            changetext()

#! 5
def ex5():
    global ddc
    global ddc2
    global user_num1
    global user_num2
    if second_num != 1:
        if ddc != 2:
            ddc = ddc + 1

        

        if ddc != 2:
            user_num1 = 5
            print(user_num1)
            changetext()
        elif ddc == 2:
            user_num1 = user_num1 * 10

            user_num1 = user_num1 + 5
            print (user_num1)
            changetext()
    elif second_num == 1:
        if ddc2 != 2:
            ddc2 = ddc2 + 1

        

        if ddc2 != 2:
            user_num2 = 5
            print(user_num2)
            changetext()
        elif ddc2 == 2:
            user_num2 = user_num2 * 10

            user_num2 = user_num2 + 5
            print (user_num2)
            changetext()
#! 6
def ex6():
    global ddc
    global ddc2
    global user_num1
    global user_num2
    if second_num != 1:
        if ddc != 2:
            ddc = ddc + 1

        

        if ddc != 2:
            user_num1 = 6
            print(user_num1)
            changetext()
        elif ddc == 2:
            user_num1 = user_num1 * 10

            user_num1 = user_num1 + 6
            print (user_num1)
            changetext()
    elif second_num == 1:
        if ddc2 != 2:
            ddc2 = ddc2 + 1

        

        if ddc2 != 2:
            user_num2 = 6
            print(user_num2)
            changetext()
        elif ddc2 == 2:
            user_num2 = user_num2 * 10

            user_num2 = user_num2 + 6
            print (user_num2)
            changetext()
#! 7
def ex7():
    global ddc
    global ddc2
    global user_num1
    global user_num2
    if second_num != 1:
        if ddc != 2:
            ddc = ddc + 1

        

        if ddc != 2:
            user_num1 = 7
            print(user_num1)
            changetext()
        elif ddc == 2:
            user_num1 = user_num1 * 10

            user_num1 = user_num1 + 7
            print (user_num1)
            changetext()
    elif second_num == 1:
        if ddc2 != 2:
            ddc2 = ddc2 + 1

        

        if ddc2 != 2:
            user_num2 = 7
            print(user_num2)
            changetext()
        elif ddc2 == 2:
            user_num2 = user_num2 * 10

            user_num2 = user_num2 + 7
            print (user_num2)
            changetext()
#! 8
def ex8():
    global ddc
    global ddc2
    global user_num1
    global user_num2
    if second_num != 1:
        if ddc != 2:
            ddc = ddc + 1

        

        if ddc != 2:
            user_num1 = 8
            print(user_num1)
            changetext()
        elif ddc == 2:
            user_num1 = user_num1 * 10

            user_num1 = user_num1 + 8
            print (user_num1)
            changetext()
    elif second_num == 1:
        if ddc2 != 2:
            ddc2 = ddc2 + 1
            changetext()

        

        if ddc2 != 2:
            user_num2 = 8
            print(user_num2)
            changetext()
        elif ddc2 == 2:
            user_num2 = user_num2 * 10

            user_num2 = user_num2 + 8
            print (user_num2)
            changetext()
#! 9
def ex9():
    global ddc
    global ddc2
    global user_num1
    global user_num2
    if second_num != 1:
        if ddc != 2:
            ddc = ddc + 1

        

        if ddc != 2:
            user_num1 = 9
            print(user_num1)
            ##used to update display
            changetext()
        elif ddc == 2:
            user_num1 = user_num1 * 10

            user_num1 = user_num1 + 9
            print (user_num1)
            ##used to update display
            changetext()
    elif second_num == 1:
        if ddc2 != 2:
            ddc2 = ddc2 + 1

        

        if ddc2 != 2:
            user_num2 = 9
            print(user_num2)
            ##used to update display
            changetext()
        elif ddc2 == 2:
            user_num2 = user_num2 * 10

            user_num2 = user_num2 + 9
            print (user_num2)
            ##used to update display
            changetext()


def exa():
    global op
    global second_num
    global opl
    second_num = 1
    op = "add"
    opl = "+"
    changetext()
def exs():
    global opl
    global op
    global second_num
    second_num = 1
    
    op = "sub"
    opl = "-"
    changetext()
def exm():
    global opl
    global second_num
    global op
    second_num = 1
    
    op = "mult"
    opl = "*"
    changetext()
def exd():
    global opl
    global op
    global second_num
    second_num = 1
    op = "divid"
    opl = "/"
    changetext()
def exmd():
    global opl
    global op
    global second_num
    second_num = 1
    
    op = "mod"
    opl = "%"
    changetext()
def exp():
    global opl
    global op
    global second_num
    second_num = 1
    
    op = "pwr"
    opl = "^"
    changetext()


def ent():
    global opl
    global op
    global answer
    if op == "add":
        answer = float(user_num1) + float(user_num2)
        
        changetext()
    elif op == "sub":
        answer = float(user_num1) - float(user_num2)
        
        changetext()
    elif op == "mult":
        answer = float(user_num1) * float(user_num2)
        
        changetext()
    elif op == "divid":
        answer = float(user_num1) / float(user_num2)
        
        changetext()
    elif op == "mod":
        answer = float(user_num1) % float(user_num2)
        
        changetext()
    elif op == "pwr":
        answer = float(user_num1) ** float(user_num2)
        
        changetext()
    print(answer)

    label = Label(root, text="your answer is " + str(answer))
    label.place(x=10,y=350)

height=3
width=5
root = Tk()

root.geometry('300x400')

num1 = Button(root, text="1", height=height, width=width, command = ex1)
num2 = Button(root, text="2", height=height, width=width, command = ex2)
num3 = Button(root, text="3", height=height, width=width, command = ex3)
num4 = Button(root, text="4", height=height, width=width, command = ex4)
num5 = Button(root, text="5", height=height, width=width, command = ex5)
num6 = Button(root, text="6", height=height, width=width, command = ex6)
num7 = Button(root, text="7", height=height, width=width, command = ex7)
num8 = Button(root, text="8", height=height, width=width, command = ex8)
num9 = Button(root, text="9", height=height, width=width, command = ex9)
num0 = Button(root, text="0", height=height, width=width, command = ex0)

opa = Button(root, text="+", height=height, width=width, command = exa)
ops = Button(root, text="-", height=height, width=width, command = exs)
opm = Button(root, text="*", height=height, width=width, command = exm)
opd = Button(root, text="/", height=height, width=width, command = exd)
opmd = Button(root, text="%", height=height, width=width, command = exmd)
opp = Button(root, text="^", height=height, width=width, command = exp)

ent = Button(root, text="enter", height=3, width=20, command = ent)



lnum = Label(root, text=" ")

def changetext():
    lnum.configure(text=str(user_num1) + str(opl) + str(user_num2) + "=" + str(answer) )

lnum.text = StringVar()


yrow1 = 50
yrow2 = 110
yrow3 = 170
yrow4 = 230

xcol1 = 10
xcol2 = 60
xcol3 = 110
xcol4 = 160

lnum.place(x=10, y=20)

ent.place(x=10, y=290)

opa.place(x=xcol4, y=yrow1)
ops.place(x=xcol4, y=yrow2)
opm.place(x=xcol4, y=yrow3)
opd.place(x=xcol4, y=yrow4)
opmd.place(x=xcol2, y=yrow4)
opp.place(x=xcol3, y=yrow4)


num1.place(x=xcol1, y=yrow1)
num2.place(x=xcol2, y=yrow1)
num3.place(x=xcol3, y=yrow1)
num4.place(x=xcol1, y=yrow2)
num5.place(x=xcol2, y=yrow2)
num6.place(x=xcol3, y=yrow2)
num7.place(x=xcol1, y=yrow3)
num8.place(x=xcol2, y=yrow3)
num9.place(x=xcol3, y=yrow3)
num0.place(x=xcol1, y=yrow4)

root.mainloop()