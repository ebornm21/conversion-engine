#A simple calculator that can compute the square of an integer.

def main():
    while True:
        try:
            x = int(input("What's x? "))
            break
        except ValueError:
            print("We need an integer here.")
    print("x squared is", square(x))


def square(n):
    return n * n

main()
