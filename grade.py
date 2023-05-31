#A program that will determine the letter grade based on the score.

while True:
    try:
        score = float(input("Score: "))
        break
    except ValueError:
        print("We need a number here.")

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")