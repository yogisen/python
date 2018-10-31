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
            "Tortilla",
            "Chicken",
            "Onion",
            "Pepper",
        ]
    },
}

print("Welcome to Python TexMex!")

food = "Tapas"
if food not in menu:
    print("We don't have this meal")
else:
    print("Here is your meal ", food)


