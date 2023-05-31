#A simple program illustrating and experimenting on the different funtions of the "random" library.

import random

coin = random.choice(["heads", "tails"])
print(coin)

number = random.randint(1, 10)
print(number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card, sep=" ")