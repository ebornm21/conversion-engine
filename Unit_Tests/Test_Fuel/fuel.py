#A direct copy of fuel.py from the Exceptions unit.

def main():
    meter = input("How full is the tank? ")
    z = convert(meter)
    output = gauge(z)
    print(output)

def convert(fraction):
    while True:
        try:
            x, y = fraction.split(sep="/")
            z = int(x) / int(y) * 100
            if z <= 100:
                return z
        except ValueError:
            print("Please enter a valid fraction")
            continue
        except ZeroDivisionError:
            print("Please enter a valid fraction")
            continue

def gauge(percentage):
    if percentage <= 1:
        return("E")
    elif percentage >= 99:
        return("F")
    else:
        return(f"{percentage:.0f}%")


if __name__ == "__main__":
    main()