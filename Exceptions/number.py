#A program that will simply get and return and integer while detecting an error if the input was not an integer and returning such information.

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            print("x is not an integer")


main()
