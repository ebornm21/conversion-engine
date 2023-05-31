#A simple program that will compare the equality of two numbers.

while True:
    try:
        x = float(input("What's x? "))
        break
    except ValueError:
        print("We need a number here.")
while True:
    try:
        y = float(input("What's y? "))
        break
    except ValueError:
        print("We need a number here.")

if x == y:
    print ("x is equal to y")
else:
    print ("x is not equal to y")
