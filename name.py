#A simple program illustrating the capabilities of the "sys" library and its argument values.

import sys

#Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    #Print name tags
    print("Hello, my name is", arg)
