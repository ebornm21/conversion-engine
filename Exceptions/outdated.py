#A program that asks for a date in month, day, year format and then converts and returns it in month, day, year format.

while True:
    # get user input date
    userinput = input("What's the date? ")

    if "/" in userinput:
        m, d, y = userinput.strip().split(sep="/")
        if m.isalpha():
            continue
        if int(m) > 12:
            continue
        if int(d) > 31:
            continue
        else:
            m = m.zfill(2)
            d = d.zfill(2)
            #print in correct order
            print(y, "-", m, "-", d, sep="")
            break

    #if date w/ words, make index of months (start with filler word as 0)
    elif "," in userinput:
        #assign month to number
        userinput = userinput.strip().replace(",", "")
        m, d, y = userinput.split(sep=" ")
        if d.isalpha():
            continue
        if m == "January":
            m = "1"
        if m == "February":
            m = "2"
        if m == "March":
            m = "3"
        if m == "April":
            m = "4"
        if m == "May":
            m = "5"
        if m == "June":
            m = "6"
        if m == "July":
            m = "7"
        if m == "August":
            m = "8"
        if m == "September":
            m = "9"
        if m == "October":
            m = "10"
        if m == "November":
            m = "11"
        if m == "December":
            m = "12"
        if int(d) > 31:
            continue
        else:
            m = m.zfill(2)
            d = d.zfill(2)
            #print in correct order
            print(y, "-", m, "-", d, sep="")
            break
    else:
        continue
