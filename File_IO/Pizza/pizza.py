#A program that will take the contents of a csv file and turn it into a formatted table.

import csv
from tabulate import tabulate
import sys


def main():
    check_arg()
    try:
        file = open(sys.argv[1], "r")
    except:
        print("File does not exist")
        sys.exit(1)
    list = []
    reader = csv.reader(file)
    for line in reader:
        list.append(line)
    print(tabulate(list[1:], headers=list[0], tablefmt="grid"))


def check_arg():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    if ".csv" not in sys.argv[1]:
        print("Not a CSV file")
        sys.exit(1)


if __name__ == "__main__":
    main()
