#A program that will detect the number of lines of code in any given program.

import sys

def main():
    check_arg()
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
    count = 0
    for line in lines:
        if check_line(line) == True:
            count += 1
    print(count)


def check_arg():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    if ".py" not in sys.argv[1]:
        print("Not a Python file")
        sys.exit(1)

def check_line(line):
    if len(line.strip()) == 0:
        return False
    if line.lstrip().startswith("#"):
        return False
    return True


if __name__ == "__main__":
    main()
