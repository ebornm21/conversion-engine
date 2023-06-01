#A program utilizing libraries in order to simulate the FIGlet program using command line arguments.

import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandomFont = False
else:
    print("Invalid usage")
    sys.exit(1)

figlet.getFonts()

if isRandomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    if sys.argv[1] == "-f" or sys.argv[1] == "-font":
        font = random.choice(figlet.getFonts())
    else:
        print("Invalid usage")
        sys.exit()

userinput = input("Input: ")
print(figlet.renderText(userinput))
