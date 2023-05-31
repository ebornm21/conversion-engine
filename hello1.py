# ask user for their name
name = input ("What's your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# say hello to user
print ("Hello, " + name)
print ("Hello,", name)
print ("Hello, ", end="")
print (name)
print ("Hello,", name, sep='???')
print ("Hello, \"friend\"")

# Remove whitespace from str and capitalize user's name
name = name.strip().title()
print (f"Hello, {first}")
