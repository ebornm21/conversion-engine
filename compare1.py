#A simple program that will compare the value of two inputted numbers.

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

if x < y:
    print ("x is less than y")
elif x > y:
    print ("x is greater than y")
else:
    print ("x is equal to y")