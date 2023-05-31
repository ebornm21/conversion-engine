#A simple program that will determine if a given number has parity.

while True:
    try:
        x = int(input("What's x? "))
        break
    except:
        print("We need an integer here.")

if x % 2 == 0:
    print("Even")
else:
    print("Odd")