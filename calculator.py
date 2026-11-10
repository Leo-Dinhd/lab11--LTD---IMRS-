import math


def square_root(a):
    try:
        if a < 0:
            raise ValueError("square_root is undefined for negative numbers")
        return math.sqrt(a)
    except TypeError:
        raise ValueError("square_root requires a number")


def hypotenuse(a, b):
    return math.hypot(a, b)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("a cannot be zero")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("need base a > 0, a != 1, and b > 0")
    return math.log(b, a)

def exponent(a, b):
    return a ** b