#An exercise using a dictionary that will pull the calorie count of a fruit of the user's choosing.

fruits = {
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Cantaloupe": 50,
    "Grapefruit": 60,
    "Grapes": 90,
    "Honeydew Melon": 50,
    "Kiwi": 90,
    "Lemon": 15,
    "Lime": 20,
    "Nectarine": 60,
    "Orange": 80,
    "Peach": 60,
    "Pear": 100,
    "Pineapple": 50,
    "Plums": 70,
    "Strawberries": 50,
    "Sweet Cherries": 100,
    "Tangerine": 50,
    "Watermelon": 80
}

userinput = input("Fruit: ").strip().title()
for fruit in fruits:
    if userinput in fruit:
        print("Calories: ", fruits[fruit])
        break
for fruit in fruits:
    if userinput not in fruits:
        print("Sorry, we don't have that one in our dictionary yet!")
        break
