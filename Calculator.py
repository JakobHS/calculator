print("Calculator")
def addition(a, b):
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
