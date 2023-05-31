#A program that uses a library to validate a user-given email address. 

from validator_collection import validators, errors


def main():
    print(check_email(input("What is your email address? ")))

def check_email(s):
    try:
        s = validators.email(s)
    except errors.InvalidEmailError:
        return "Invalid"
    except ValueError:
        return "Invalid"
    return "Valid"


if __name__ == "__main__":
    main()