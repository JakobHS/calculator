import tkinter as tk
# creating tk window
window = tk.Tk()
window.title("calculator")

def handle_click(event):
    print(button['text'])

Screen = tk.Frame(
    master = window,
    borderwidth= 5
)
Screen.pack()

labels = ['1', '2', '3', '+',
          '4', '5', '6', '-',
          '7', '8', '9', '*',
          '.', '0', 'ans', '/']

labelmain = tk.Label(
    text = 'jekfsef',
    master = Screen,
    width= 15,
    relief= tk.SUNKEN,
    height= 2,
    anchor = 'e',
    padx= 10,
    font = ('Arial', 17)
)
labelmain.pack()


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
    bg= 'white',
    command = handle_click
)
b2 = tk.Button(
    text="2",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'white',
    command = handle_click
)
b3 = tk.Button(
    text="3",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'white',
    command = handle_click
)
b4 = tk.Button(
    text="+",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'gray',
    command = handle_click
)
b5 = tk.Button(
    text="4",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'white',
    command = handle_click
)
b6 = tk.Button(
    text="5",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'white',
    command = handle_click
)
b7 = tk.Button(
    text="6",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'white',
    command = handle_click
)
b8 = tk.Button(
    text="-",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'gray',
    command = handle_click
)
b9 = tk.Button(
    text="7",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'white',
    command = handle_click
)
b10 = tk.Button(
    text="8",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'white',
    command = handle_click
)
b11 = tk.Button(
    text="9",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'white',
    command = handle_click
)
b12 = tk.Button(
    text="*",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'gray',
    command = handle_click
)
b13 = tk.Button(
    text=".",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'gray',
    command = handle_click
)
b14 = tk.Button(
    text="0",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'white',
    command = handle_click
)
b15 = tk.Button(
    text="ans",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'orange',
    command = handle_click
)
b16 = tk.Button(
    text="/",
    master = frame,
    height= 3,
    width= 5,
    borderwidth=5,
    relief= tk.RIDGE,
    bg= 'gray',
    command = handle_click
)

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