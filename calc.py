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


        if x == "e":
            x = float(math.e)
        if y == "e":
            x = float(math.e)


        if x == tau
            x = float(math.tau)
        if y == tau
            y = float(math.tau)

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
            print("\n ", x, "+", y, "=", add(x, y))

        elif choice == "subtraction":
            print("\n ", x, "-", y, "=", subtract(x, y))

        elif choice == "multiplication":
            print("\n ", x, "*", y, "=", multiply(x, y))

        elif choice == "division":
            print("\n ", x, "/", y, "=", divide(x, y))

        elif choice == "exponents":
            print("\n ", x, "^", y, "=", exponent(x, y))

        elif choice == "nth root":
            print("\n ", "^", x, "√", y, "=", nthroot(x, y))

        elif choice == "logarithm":
            print("\n ", f'log({x} [, {y}]) = ', log(x, y)) #THANK YOU CAFF!!!

        elif choice == "modulo":
            print("\n ", x, "%", y, "=", modulo(x, y))

        else:
            print("Invalid Input")


#1 choice ####################
    if choice in ("square root", "sine", "cosine", "tangent", "cotangent", "secant", "cosecant"):
        x = float(input("Enter first number: "))

        if choice == "square root":
            print("\n ","√", x, "=", sqrt(x))

        elif choice == "sine":
            print("\n ", f'sin({x}) = ', sine(x))

        elif choice == "cosine":
            print("\n ", f'cos({x}) = ', cosine(x))

        elif choice == "tangent":
            print("\n ", f'tan({x}) = ', tangent(x))

        elif choice == "cotangent":
            print("\n ", f'cot({x}) = ', cotangent(x))

        elif choice == "secant":
            print("\n ", f'sec({x}) = ', secant(x))

        elif choice == "cosecant":
            print("\n ", f'csc({x}) = ', cosecant(x))

        else:
            print("Invalid Input")
