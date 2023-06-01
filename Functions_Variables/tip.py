#A simple program that will calculate the desired tip for you.

def main():
    while True:
        try:
            dollars = dollars_to_float(input("How much was the meal? "))
            break
        except ValueError:
            print("Please enter the amount you paid")
    while True:
        try:
            percent = percent_to_float(input("What percentage would you like to tip? "))
            break
        except ValueError:
            print("Please enter the percent amount you would like to tip")
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    ddec = d.replace("$", "")
    return float(ddec)

def percent_to_float(p):
    pplain = p.replace("%", "")
    pdec = float(pplain) / 100
    return pdec

main()
