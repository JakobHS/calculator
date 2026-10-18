import tkinter as tk
# creating tk window
window = tk.Tk()
window.title("calculator")

frame = tk.Frame(
    master=window,
    borderwidth=2)

#creating all buttons
b1 = tk.Button(
    text="1",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'white'
)
b2 = tk.Button(
    text="2",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'white'
)
b3 = tk.Button(
    text="3",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'white'
)
b4 = tk.Button(
    text="+",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'gray'
)
b5 = tk.Button(
    text="4",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'white'
)
b6 = tk.Button(
    text="5",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'white'
)
b7 = tk.Button(
    text="6",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'white'
)
b8 = tk.Button(
    text="-",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'gray'
)
b9 = tk.Button(
    text="7",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'white'
)
b10 = tk.Button(
    text="8",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'white'
)
b11 = tk.Button(
    text="9",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'white'
)
b12 = tk.Button(
    text="*",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'gray'
)
b13 = tk.Button(
    text=".",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'gray'
)
b14 = tk.Button(
    text="0",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'white'
)
b15 = tk.Button(
    text="ans",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'orange'
)
b16 = tk.Button(
    text="/",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'gray'
)

labelmain = tk.Label(
    text = 'jekfsef',
    width= 32,
    relief= tk.SUNKEN,
    height= 4
)
labelmain.pack()

buttons_dics = {1:b1, 2:b2, 3:b3, 4:b4, 5:b5, 6:b6, 7:b7, 8:b8, 9:b9, 10:b10, 11:b11, 12:b12, 13:b13, 14:b14, 15:b15, 16:b16}

num = 0
for i in range(4):
    for j in range(4):
        num += 1
        button = buttons_dics[num]
        button.grid(row = i, column = j, padx= 5, pady=5)

frame.pack(padx= 5, pady=5)

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