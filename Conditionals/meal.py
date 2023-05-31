#A simple program designed to say what meal it is time for (or if not at all).

def main():
    time = input("What time is it in military time? ")
    times = convert(time)
    if 7.0 <= times <= 8.0:
        print("It's breakfast time")
    elif 12.0 <= times <= 13.0:
        print("It's lunch time")
    elif 18.0 <= times <= 19.0:
        print("It's dinner time")
    else:
        print("Looks like it's not time for a meal yet.")

def convert(time):
    hours, minutes = time.split(":")
    times = int(hours) + int(minutes) / 60
    return times

if __name__ == "__main__":
    main()
