#A program that will take inputs and add them to a csv file.

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students2.csv", "a", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
