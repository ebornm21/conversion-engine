#A simple calculator that can compute the theory of relativity of a given mass

while True:
    try:
        m = float(input("m: "))
        break
    except ValueError:
        print("We need a number here.")

c = 300000000

E = m * (c ** 2)

print(E)
