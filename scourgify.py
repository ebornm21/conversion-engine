#A program which takes the contents of before.csv and splits its contents and cleans them up, putting the new values into a new file called after.csv.

import csv
import sys

def main():
    check_arg()
    try:
        file = open(sys.argv[1], "r")
        reader = csv.DictReader(file)
    except:
        print(f"{sys.argv[1]} does not exist")
        sys.exit(1)
    students = []
    for row in reader:
        last, first = row["name"].split(",")
        house = row["house"]
        students.append({"first": first.lstrip(), "last": last.lstrip(), "house": house})
    with open(sys.argv[2], "w", newline="") as after:
        writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in students:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})

def check_arg():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    if ".csv" not in sys.argv[1] and ".csv" not in sys.argv[2]:
        print("Not CSV files")
        sys.exit(1)


if __name__ == "__main__":
    main()