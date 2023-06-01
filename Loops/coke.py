#A simple program that acts as a vending machine into which you can add change until the drink is paid for.

c = 50

while c > 0:
    print("Amount due: ", c)
    n = int(input("Please insert change: "))
    if n in [5, 10, 25]:
        c = int(c) - int(n)
        continue

while c <= 0:
    c = abs(c)
    print("Change owed: ", c)
    break
