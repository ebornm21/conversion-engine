#A program created in reference to "The Hitchhiker's Guide to the Galaxy", wherein the user must answer the Great Question of Life.

userinput = input("What is the answer to the Great Question of Life? ")
userinput = userinput.lower().strip()

if userinput == "42":
    print("Yes")
elif userinput == "forty-two":
    print("Yes")
elif userinput == "forty two":
    print("Yes")
else:
    print("No")
