#A program that takes a user-given input for their name and house and returns it. It detects and reassigns Padma's house to make it accurate to the books rather than the movies.

def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]


if __name__ == "__main__":
    main()