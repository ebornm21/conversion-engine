#A direct copy of bank.py from the Conditionals unit.

def main():
    greeting = input("Hello! ")
    amount = value(greeting)
    print(f"${amount}")

def value(greeting):
    greeting = greeting.lower().strip()
    if "hello" in greeting:
        return 0
    elif "h" in greeting[0]:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()