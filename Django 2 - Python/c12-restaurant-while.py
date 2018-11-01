import pprint

pp = pprint.PrettyPrinter(indent=4)

menu = {
    "Tapas": {
        "ingredients": [
            "Tomatoes",
            "Olive",
            "Fine Ham",
        ]
    },
    "Fajitas": {
        "ingredients": [
            "Tortilla"
            "Chicken",
            "Onion",
            "Pepper",
        ]
    },
}

print("Welcome to Python Tex Mex!")

run = True
while run:
    action = input("What do you want today (type \"help\" to see possible action)? ")

    if action == 'help':
        print("""
Possible actions:
"menu": to display the menu
"order <food>: to order specified food
"exit": to leave our restaurant
        """)
    elif action == "menu":
        pp.pprint(menu)
    elif action.startswith("eat"):
        _, food = action.split(" ")
        print("You ordered " + food + "! Let's see what we have...")

        if food not in menu.keys():
            print("We do not have this kind of food")
            continue

        print("Here is your meal")
        print("\n(っ˘ڡ˘)っ─∈ ~~旦_(･o･;)\n")

    elif action == 'exit':
        run = False
    else:
        print("We don't know how to process " + action + ", we're very sorry!")

print("A very good day to you!")

