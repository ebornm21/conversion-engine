#A program that can compute simple arithmetic equations.

userinput = input("What's the equation? ")
x,y,z = userinput.split()

if y == "+":
    i = int(x) + int(z)
    print(f"{i:.1f}")
elif y == "-":
    j = int(x) - int(z)
    print(f"{j:.1f}")
elif y == "*":
    k = int(x) * int(z)
    print(f"{k:.1f}")
elif y == "/":
    l = int(x) / int(z)
    print(f"{l:.1f}")
else:
    print("That equation is too complicated for me right now!")