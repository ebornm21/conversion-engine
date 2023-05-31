#A program that takes a given list and adds them to a new list while appending additional information to each entry.

students = ["Hermione", "Harry", "Ron"]

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

print(gryffindors)
