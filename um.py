#A program that will return the number of times "um" appears in a sentence. It will not count um's that appear within a word, i.e. "yummy".

import re


def main():
    print(count(input("Text: ")))

def count(s):
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    if matches:
        return len(matches)
    else:
        return 0

if __name__ == "__main__":
    main()