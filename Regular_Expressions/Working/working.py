#A program that takes an input of a time range in 12-hour format and returns it in 24-hour format.

import re


def main():
    time = input("Hours: ").strip()
    new = convert(time)
    print(new)

def convert(s):
    matches = re.search(r"^(([0-9][0-2]?):?([0-5][0-9])?) (AM|PM) to (([0-9][0-2]?):?([0-5][0-9])?) (AM|PM)$", s, re.IGNORECASE)
    if matches:
        times = matches.groups()
        if int(times[1]) > 12 or int(times[5]) > 12:
            raise ValueError
        clockin = newtime(times[1], times[2], times[3])
        clockout = newtime(times[5], times[6], times[7])
        return clockin + " to " + clockout
    else:
        raise ValueError

def newtime(hour, minute, am_pm):
    if am_pm == "PM":
        if int(hour) == 12:
            hour = 12
        else:
            hour = int(hour) + 12
    else:
        if int(hour) == 12:
            hour = 0
        else:
            hour = int(hour)
    if minute == None:
        minute = ":00"
        time = f"{hour:02}" + minute
    else:
        time = f"{hour:02}" + ":" + minute
    return time


if __name__ == "__main__":
    main()
