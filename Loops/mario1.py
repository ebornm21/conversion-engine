#A simple exercise using loops to emulate the image of a brick, in resemblance of ones seen in Mario games.

def main():
    print_column(3)


def print_column(height):
    for _ in range(height):
        print("#")


main()  
