import pprint

restaurant_menu = {
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


def print_help():
    print("""
Possible actions:
"menu": to display the menu
"order <food>: to order specified food
"exit": to leave our restaurant
""")


def print_menu(menu):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(menu)


def order_food(ordered_food):
    print("You ordered " + ordered_food + "! Let's see what we have...")

    if ordered_food not in restaurant_menu:
        print("We do not have this kind of food")
        return

    print("Here is your meal")
    print("\n(っ˘ڡ˘)っ─∈ ~~旦_(･o･;)\n")


print("Welcome to Python Tex Mex!")

run = True
while run:
    action = input("What do you want today (type \"help\" to see possible action)? ")

    if action == 'help':
        print_help()
    elif action == "menu":
        print_menu(restaurant_menu)
    elif action.startswith("eat"):
        _, food = action.split(" ")
        order_food(food)
    elif action == 'exit':
        run = False
    else:
        print("We don't know how to process " + action + ", we're very sorry!")

print("A very good day to you!")
