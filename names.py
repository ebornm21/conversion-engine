#A simple program that will compose and add names to a txt file.

name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

