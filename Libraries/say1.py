#A simple program using both the "cowsay" library and the "sys" library and illustrating how they can work together.

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
    cowsay.trex("hello, " + sys.argv[1])
