#A conversion engine that can convert between multiple units. Please see README.md for more details.

def main():
    while True:                        #Determines what unit type the user is converting between.
        type = input("What would you like to convert? (Ex. temperature, length, distance, mass) ").lower().strip()
        if type in ["temperature", "length", "mass", "distance"]:
            break
        else:
            print("Oops! We can't do that conversion yet! Please try a different one.")
            continue
    if type == "temperature":
        print(tempconvert())
    elif type == "length":
        print(lengthconvert())
    elif type == "mass":
        print(massconvert())
    elif type == "distance":
        print(distconvert())


#Main conversion function for temperature.
def tempconvert():
    while True:                        #Determines the user's starting unit.
        conv = input("What unit are you starting with? Please use standard abbreviations (C, F) ").upper().strip()
        if conv in ["C", "F"]:
            break
        else:
            print("Oops! We can't do that conversion yet! Please try a different one or check that your abbreviation is correct!")
            continue
    if conv == "C":                    #If the user's starting unit is Celsius
        while True:
            try:
                C = float(input("What is the temperature in C? I only need the number. "))
                break
            except ValueError:
                print("Sorry! We just need a number here!")
                continue
        F = (C * 9/5) + 32
        return f"{F} degrees Farenheit"
    if conv == "F":                    #If the user's starting unit is Farenheit
        while True:
            try:
                F = float(input("What is the temperature in F? I only need the number. "))
                break
            except ValueError:
                print("Sorry! We just need a number here!")
                continue
        C = (F - 32) * 5/9
        return f"{C} degrees Celsius"

#Main conversion function for length.
def lengthconvert():
    while True:                        #Determines the user's starting unit
        conv = input("What unit are you starting with? Please use standard abbreviations (in, cm) ").lower().strip()
        if conv in ["in", "cm"]:
            break
        else:
            print("Oops! We can't do that conversion yet! Please try a different one or check that your abbreviation is correct!")
            continue
    if conv == "in":                   #If the user's starting unit is inches...
        while True:
            try:
                inches = float(input("What is the length in inches? I only need the number. "))
                break
            except ValueError:
                print("Sorry! We just need a number here!")
                continue
        cm = inches * 2.54
        return f"{cm} cm"
    if conv == "cm":                   #If the user's starting unit is centimeters...
        while True:
            try:
                cm = float(input("What is the length in cm? I only need the number. "))
                break
            except ValueError:
                print("Sorry! We just need a number here!")
                continue
        inches = cm / 2.54
        return f"{inches} inches"

#Main conversion function for mass.
def massconvert():
    while True:                        #Determines the user's starting unit
        conv = input("What unit are you starting with? Please use standard abbreviations (kg, lb) ").lower().strip()
        if conv in ["kg", "lb"]:
            break
        else:
            print("Oops! We can't do that conversion yet! Please try a different one or check that your abbreviation is correct!")
            continue
    if conv == "kg":                    #If the user's starting unit is kilograms...
        while True:
            try:
                kg = float(input("What is the mass in kilograms? I only need the number. "))
                break
            except ValueError:
                print("Sorry! We just need a number here!")
                continue
        lb = kg * 2.205
        return f"{lb} pounds"
    if conv == "lb":                #If the user's starting unit is pounds...
        while True:
            try:
                lb = float(input("What is the mass in pounds? I only need the number. "))
                break
            except ValueError:
                print("Sorry! We just need a number here!")
                continue
        kg = lb / 2.205
        return f"{kg} kilograms"

#Main conversion function for distance.
def distconvert():
    while True:                    #Determines the user's starting unit
        conv = input("What unit are you starting with? Please use standard abbreviations (km, mi) ").lower().strip()
        if conv in ["km", "mi"]:
            break
        else:
            print("Oops! We can't do that conversion yet! Please try a different one or check that your abbreviation is correct!")
            continue
    if conv == "km":                #If the user's starting unit is kilograms...
        while True:
            try:
                km = float(input("What is the distance in kilometers? I only need the number. "))
                break
            except ValueError:
                print("Sorry! We just need a number here!")
                continue
        mi = km * 0.621371
        return f"{mi} miles"
    if conv == "mi":                #If the user's starting unit is miles...
        while True:
            try:
                mi = float(input("What is the distance in miles? I only need the number. "))
                break
            except ValueError:
                print("Sorry! We just need a number here!")
                continue
        km = mi / 0.621371
        return f"{km} kilometers"


if __name__ == "__main__":
    main()
