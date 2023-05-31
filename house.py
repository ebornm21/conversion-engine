#A program that takes a user inputted name and matches that name to the character's house and returns it, showing an error when an excepted input is not given.

name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")