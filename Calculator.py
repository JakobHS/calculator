import tkinter as tk
# creating tk window
window = tk.Tk()

#creating all labels
title = tk.Label(
    text="Super Calculator",
    width=20,
    bg= 'red',
    fg= 'white')
title.pack()

#creating all buttons
b1 = tk.Button(
    text="1",
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'white'
)
b1.pack()

window.mainloop()


print("Calculator")
'''def addition(a, b):
    return a+b
def subtraction(a, b):
    return a-b
def multiplication(a, b):
    return a*b
def division(a, b):
    return a/b, a%b

a = int(input("first number "))
equ = (input("input type of equation "))
b = int(input("second number "))
if equ == "+":
    print(addition(a, b))
if equ == "-":
    print(subtraction(a, b))
if equ == "*":
    print(multiplication(a, b))
if equ == "/":
    print(division(a, b))
'''