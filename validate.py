#A program that will parse an inputted email and determine if it is valid or not.

import re

email = input("What's your email? ").strip()

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")