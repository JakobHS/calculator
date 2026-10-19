import tkinter as tk
# creating tk window
window = tk.Tk()
window.title("calculator")

Screen = tk.Frame(
    master = window,
    borderwidth= 5
)
Screen.pack()

frame = tk.Frame(
    master=window,
    borderwidth=2
)
frame.pack()


labelmain = tk.Label(
    text = '',
    master = Screen,
    width= 15,
    relief= tk.SUNKEN,
    height= 2,
    anchor = 'e',
    padx= 10,
    font = ('Arial', 17)
)
labelmain.pack()

def solve(sequ):
    if '/' in sequ:
        a = float(sequ[sequ.index('/') -1])
        b = float(sequ[sequ.index('/') +1])
        c = a / b
        sequ[sequ.index('/')] = (str(c))
        del sequ[sequ.index(str(c)) -1]
        del sequ[sequ.index(str(c)) +1]

    elif '*' in sequ:
        a = float(sequ[sequ.index('*') -1])
        b = float(sequ[sequ.index('*') +1])
        c = a * b
        sequ[sequ.index('*')] = (str(c))
        del sequ[sequ.index(str(c)) -1]
        del sequ[sequ.index(str(c)) +1]

    elif '-' in sequ:
        a = float(sequ[sequ.index('-') -1])
        b = float(sequ[sequ.index('-') +1])
        c = a - b
        sequ[sequ.index('-')] = (str(c))
        del sequ[sequ.index(str(c)) -1]
        del sequ[sequ.index(str(c)) +1]

    elif '+' in sequ:
        a = float(sequ[sequ.index('+') -1])
        b = float(sequ[sequ.index('+') +1])
        c = a + b
        sequ[sequ.index('+')] = (str(c))
        del sequ[sequ.index(str(c)) -1]
        del sequ[sequ.index(str(c)) +1]
    return sequence


sequence = []
def handle_click(text):
    if text == 'ans':
        solve(sequence)
        labelmain['text'] = sequence
    elif text in '123456789':
        labelmain['text'] = labelmain['text'] + text
        num = (text)
        sequence.append(num)
    else:
        labelmain['text'] = labelmain['text'] + text
        equ = text
        sequence.append(equ)

labels = ['1', '2', '3', '+',
          '4', '5', '6', '-',
          '7', '8', '9', '*',
          '.', '0', 'ans', '/']

for num, text in enumerate(labels):
    if text == 'ans':
        colour = 'orange'
    elif text in '1234567890':
        colour = 'white'
    else:
        colour = 'gray'
    button = tk.Button(
        text=text,
        master = frame,
        height= 3,
        width= 5,
        borderwidth=5,
        relief= tk.RIDGE,
        bg= colour,
        command=lambda t=text: handle_click(t)
    )
    button.grid(
        row=num // 4,
        column=num % 4,
        padx=5,
        pady=5
    )

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