#A program that will continue adding names to a list, which when completed, will say adieu to all of them, as is done in "The Sound of Music".

import inflect
p = inflect.engine()

d = []

while True:
    try:
        name = input().strip().title()
        d.append(name)
        continue
    except EOFError:
        break

names = p.join((d))
print(f"Adieu, adieu, to {names}")