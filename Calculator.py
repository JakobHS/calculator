import tkinter as tk
# creating tk window
window = tk.Tk()
window.title("calculator")

#creating all buttons
b1 = tk.Button(
    text="1",
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'white'
)
#b1.pack()
num = 0
for i in range(4):
    for j in range(4):
        frame = tk.Frame(
            master=window,
            relief = tk.RIDGE,
            borderwidth=2)
        num += 1
        frame.grid(row = i, column = j, padx= 5, pady=5)
        button = tk.Button(relief = tk.RIDGE, master = frame, text = f'space {num}')
        button.pack(padx= 5, pady=5)

window.mainloop()


print("it worked!")
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