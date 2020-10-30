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

def sqrt(x): #lmfao wtf is this logic lmaooo how does this not just return x ahahahhaa
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

def isinfinite(x):
    return mpmath.isinf(x)

def isNaN(x):
    return mpmath.isnan(x)

def absVal(x):
    return mpmath.fabs(x)

def floor(x):
    return mpmath.floor(x)

def ceil(x):
    return mpmath.ceil(x)

def nInt(x):
    return mpmath.nint(x)

def factorial(x):
    return mpmath.factorial(x)

def reinputNum(num):
    if num == "pi":
        num = float(math.pi)
        return float(num)
    elif num == "e":
        num = float(math.e)
        return float(num)
    elif num == "tau":
        num = float(math.tau)
        return float(num)
    elif num == "phi":
        num = float(mpmath.phi)
        return float(num)

    #print(type(num)) ----------------- dont use rn

    while True:
        try:
            num = float(num)
            return float(num)
        except ValueError:
            print(" Invalid input")
            num = input(" Re-enter your number: ")


print("\n Select an operation:\n")
multiline_str = ("\n    addition (+)\n    subtraction (-)\n    multiplication (*)\n    division (/)\n"
   "    exponents (^)\n    square root (sqrt)\n    nth root (nthroot)\n    logarithm (log)\n    modulo (mod)\n"
   "    sine (sin)\n    cosine (cos)\n    tangent (tan)\n    cotangent (cot)\n    secant (sec)\n    cosecant (csc)\n"
   "    is infinite (isinf)\n    is not-a-number (isNaN)\n    absolute value (abs)\n    floor (floor)\n    ceiling (ceil)\n"
   "    nearest integer (nint)\n    factorial (fac)")

print(multiline_str)

while True:
    # User input
    print("\n")
    choice = input(" Enter operation name: ")


    #2 choice ###################################
    # Check if choice is one of the options
    if choice in ("+", "-", "*", "/", "^", "nthroot", "log", "mod"):
        x = input(" Enter first number: ")
        x = reinputNum(x)

        y = input(" Enter second number: ")
        y = reinputNum(y)


        if choice == "+":
            print("\n   ", x, "+", y, "=", add(x, y))

        elif choice == "-":
            print("\n   ", x, "-", y, "=", subtract(x, y))

        elif choice == "*":
            print("\n   ", x, "*", y, "=", multiply(x, y))

        elif choice == "/":
            print("\n   ", x, "/", y, "=", divide(x, y))

        elif choice == "^":
            print("\n   ", x, "^", y, "=", exponent(x, y))

        elif choice == "nthroot":
            print("\n   ", "^", x, "√", y, "=", nthroot(x, y))

        elif choice == "log":
            print("\n   ", f'log({x} [, {y}]) = ', log(x, y)) #THANK YOU CAFF!!!

        elif choice == "mod":
            print("\n   ", x, "%", y, "=", modulo(x, y))

        else:
            print(" Invalid Input.")


#1 choice ####################
    if choice in ("sqrt", "sin", "cos", "tan", "cot", "sec", "csc", "isinf", "isNaN", "abs", "floor", "ceil", "nint", "fac"):
        x = float(input(" Enter first number: "))

        if choice == "sqrt":
            print("\n   ","√", x, "=", sqrt(x))

        elif choice == "sin":
            print("\n   ", f'sin({x}) = ', sine(x))

        elif choice == "cos":
            print("\n   ", f'cos({x}) = ', cosine(x))

        elif choice == "tan":
            print("\n   ", f'tan({x}) = ', tangent(x))

        elif choice == "cot":
            print("\n   ", f'cot({x}) = ', cotangent(x))

        elif choice == "sec":
            print("\n   ", f'sec({x}) = ', secant(x))

        elif choice == "csc":
            print("\n   ", f'csc({x}) = ', cosecant(x))

        elif choice == "isinf":
            print("\n   ", f'isinf({x}) = ', isinfinite(x))

        elif choice == "isNaN":
            print("\n   ", f'isNaN({x}) = ', isNaN(x))

        elif choice == "abs":
            print("\n   ", f'abs({x}) = ', absVal(x))

        elif choice == "floor":
            print("\n   ", f'floor({x}) = ', floor(x))

        elif choice == "ceil":
            print("\n   ", f'ceil({x}) = ', ceil(x))

        elif choice == "nint":
            print("\n   ", f'nint({x}) = ', nInt(x))

        elif choice == "fac":
            print("\n   ", f'fac({x}) = ', factorial(x))

        else:
            print(" Invalid Input.")

            positive_infnity = float('inf')
            print(positive_infnity)

            negative_infnity = float('-inf')
            print(negative_infnity)
