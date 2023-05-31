#A program that uses a library in order to convert emoticons into emojis.

import emoji

# get user input
userinput = input("Input: ")

#convert to emoji
emoji = emoji.emojize(userinput)

#print output
print(f"Output: {emoji}")