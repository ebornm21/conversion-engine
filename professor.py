#A program that will emulate the "Little Professor" game, which gives ten randomly generated addition problems for the user to solve and their score.

import random

def main():
    level = get_level()
    correct = simulate_game(level)
    print(f"Score: {correct}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
        except ValueError:
            pass
    return level

def generate_integer(level):
    if level == 1:
        a = random.randint(0,9)
        b = random.randint(0,9)
    elif level == 2:
        a = random.randint(10,99)
        b = random.randint(10,99)
    elif level == 3:
        a = random.randint(100,999)
        b = random.randint(100,999)
    return a,b

def simulate_round(a, b):
    tries = 0
    while tries < 3:
        try:
            guess = int(input(f"{a} + {b} = "))
            if guess == (a + b):
                return True
            else:
                tries = tries + 1
                print("EEE")
        except ValueError:
            print("EEE")
            tries = tries + 1
    print(f"{a} + {b} = {a+b}")
    return False

def simulate_game(level):
    count = 0
    correct = 0
    while (count < 10):
        a, b = generate_integer(level)
        count = count + 1
        response = simulate_round(a, b)
        if response == True:
            correct = correct + 1
    return correct

if __name__ == "__main__":
    main()