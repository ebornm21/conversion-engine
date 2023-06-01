#A simple program that returns an input using a more defined funtion.

def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("Hello,", to)

main()
