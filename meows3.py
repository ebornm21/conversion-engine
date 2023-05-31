#A program that meows a user-specified number of times. It includes a help function and and argument parser to make the program run more effectively.

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")