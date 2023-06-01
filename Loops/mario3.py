#An exercise that utilizes loops to create a group of bricks, in remblance of those in Mario games.

def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)


main()
