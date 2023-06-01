#A simple game that will have the user try to guess a randomly selected number, prompting the user if their input is too small, too large, or just right until the correct answer is acheived.

import random

while True:
    try:
        b = int(input("Level: "))
        if b <= 0:
            continue
        break
    except ValueError:
        continue

number = random.randint(1, b)


while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    else:
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        elif guess == number:
            print("Just right!")
            break
