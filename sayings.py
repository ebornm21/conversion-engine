#A simple program in which two (rather small) libraries were created and utilized.

def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"Hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


if __name__ == "__main__":
    main()