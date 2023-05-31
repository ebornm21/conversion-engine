#A program created in reference to the Seinfield episode in which Kramer goes to the bank and is awarded based on the teller's greeting.

def main():
    greeting = input("Hello! ").lower().strip()
    amount = value(greeting)
    print(amount)

def value(greeting):
    if greeting.startswith("hello") == True:
        amount = "$0"
        return amount
    elif greeting.startswith("h") == True:
        amount = "$20"
        return amount
    else:
        amount = "$100"
        return amount


if __name__ == "__main__":
    main()