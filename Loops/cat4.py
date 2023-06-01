#Another exercise in using loops to cause a repeat in information, this time with user input.

while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
