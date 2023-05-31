#A simple program that will determine the parity of a given number.

def main():
    while True:
        try:
            x = int(input("What's x? "))
            break
        except ValueError:
            print("We need an integer here.")
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()