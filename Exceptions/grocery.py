#A program that will create a shopping list. It will then sort the list and count the number of times a list item was inputted and display the count.

#Create dictionary
d = {}

#Loop forever
while True:
    try:
        #get user input
        item = input().strip().upper()

        #Check if already in dictionary, add one to count
        if item in d:
            d[item] += 1

        #Otherwise, add item for first time
        else:
            d[item] = 1
        continue

    except EOFError:
        #stop the while loop
        break
    
#Print all items in alphabetical order
for key in sorted(d.keys()):
    print(d[key], key)
