#A direct copy of plates.py from the Loops unit.

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s)>6:
        return False
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            elif s[i:].isdigit() == False:
                return False
            else:
                break
        i += 1
    for character in s:
        if character in [",", ".", "!", "?"]:
            return False
    return True

if __name__ == "__main__":
    main()
