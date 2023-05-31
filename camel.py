#A simple program that convert any given input from snake case to camel case.

camel = input("input camelCase: ")

for letter in camel:
    if letter.isupper():
        print("_" + letter.lower(), end="")
    else:
        print(letter, end="")
print()