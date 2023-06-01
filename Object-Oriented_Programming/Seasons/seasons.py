#A program that will take the user's date of birth and tell them how old they are in minutes, rounded to the nearest integer. It will assume midnight for both the time of birth and today.

from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    d = input("Date of Birth: ")
    print(convert(d))


def convert(d):
    today = date.today()
    try:
        year, month, day = d.split("-")
        bday = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")
    time_from_bday = abs(today - bday)
    min = int(time_from_bday.days) * 1440
    minutes = p.number_to_words(min, andword="").capitalize()
    return f"{minutes} minutes"


if __name__ == "__main__":
    main()
