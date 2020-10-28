import math

import mpmath

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def exponent(x, y):
    return (x ** y)

def sqrt(x):
    return(x)**(1/2)

def nthroot(x, y):
    return pow(y,(1/x))

def log(x, y):
    return math.log(y, x)

def modulo(x, y):
    return x % y

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def tangent(x):
    return math.tan(x)

def cotangent(x):
    return mpmath.cot(x)

def secant(x):
    return mpmath.sec(x)

def cosecant(x):
    return mpmath.csc(x)

print("Select an operation:\n")
multiline_str = ("\n   addition\n   subtraction\n   multiplication\n   division\n"
   "   exponents\n   square root\n   nth root\n   logarithm\n   modulo\n"
   "   sine\n   cosine\n   tangent\n   cotangent\n   secant\n   cosecant\n")

print(multiline_str)


while True:
    # User input
    choice = input("\nEnter operation's name: ")


    #2 choice ###################################
    # Check if choice is one of the options
    if choice in ("addition", "subtraction", "multiplication", "division", "exponents", "nth root", "logarithm", "modulo"):
        x = str(input("Enter first number: "))
        y = str(input("Enter second number: "))

        if x == "pi":
            x = float(math.pi)

        if y == "pi":
            y = float(math.pi)

#        try:
#            x = float(x)
#        except:
#            print("Your first number is invalid. Please enter a valid number.")
#            x = str(input("Enter first number: "))
#            y = float(y)
#        except:
#            print("Your first number is invalid. Please enter a valid number.")
#            y = str(input("Enter second number: "))


        if choice == "addition":
            print(" ", x, "+", y, "=", add(x, y))

        elif choice == "subtraction":
            print(" ", x, "-", y, "=", subtract(x, y))

        elif choice == "multiplication":
            print(" ", x, "*", y, "=", multiply(x, y))

        elif choice == "division":
            print(" ", x, "/", y, "=", divide(x, y))

        elif choice == "exponents":
            print(" ", x, "^", y, "=", exponent(x, y))

        elif choice == "nth root":
            print(" ", "^", x, "√", y, "=", nthroot(x, y))

        elif choice == "logarithm":
            print(" ", f'log({x} [, {y}]) = ', log(x, y)) #THANK YOU CAFF!!!

        elif choice == "modulo":
            print(" ", x, "%", y, "=", modulo(x, y))

        else:
            print("Invalid Input")


#1 choice ####################
    if choice in ("square root", "sine", "cosine", "tangent", "cotangent", "secant", "cosecant"):
        x = float(input("Enter first number: "))

        if choice == "square root":
            print(" ","√", x, "=", sqrt(x))

        elif choice == "sine":
            print(" ", f'sin({x}) = ', sine(x))

        elif choice == "cosine":
            print(" ", f'cos({x}) = ', cosine(x))

        elif choice == "tangent":
            print(" ", f'tan({x}) = ', tangent(x))

        elif choice == "cotangent":
            print(" ", f'cot({x}) = ', cotangent(x))

        elif choice == "secant":
            print(" ", f'sec({x}) = ', secant(x))

        elif choice == "cosecant":
            print(" ", f'csc({x}) = ', cosecant(x))

        else:
            print("Invalid Input")
