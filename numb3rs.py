#A program that can take a given input and determine if it is a valid IP address.

import re


def main():
    ip = input("IPv4 Address: ")
    test = validate(ip)
    print(test)

def validate(ip):
    try:
        matches = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
        numbers = [matches.group(1), matches.group(2), matches.group(3), matches.group(4)]
        for number in numbers:
            if 0 > int(number) or int(number) > 255:
                return False
        return True
    except:
        print("False")
        exit()


if __name__ == "__main__":
    main()