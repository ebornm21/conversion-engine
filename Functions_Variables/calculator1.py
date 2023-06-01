#A simple calculator that computes the quotient of two numbers.

from tkinter import Y


while True:
    try:
        x = float(input("What's x? "))
        break
    except ValueError:
        print("We need a number here")
while True:
    try:
        y = float(input("What's y? "))
        break
    except ValueError:
        print("We need a number here.")

z = x / y

print (f"{z:.2f}")
