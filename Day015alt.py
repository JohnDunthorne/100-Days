# Using pycharm environment
# installed
# coffee machine
from sys import exit

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

water_left = (resources['water'])
milk_left = (resources['milk'])
coffee_left = (resources['coffee'])
# TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

while True:
    choice = input(f"“What would you like? (espresso/latte/cappuccino):”\n").lower()
    if choice in MENU:
        drink_ingredients = MENU[choice]['ingredients']
        for ingredient, amount in drink_ingredients.items():
            print(ingredient, amount)
    elif choice == 'off':
        exit()
    elif choice == 'report':
        print(f"water = {water_left}\n"
              f"milk = {milk_left}\n"
              f"coffee = {coffee_left}")
    else:
        print("invalid input")



# TODO: Turn off the Coffee Machine by entering “off” to the prompt
# TODO: Print report.


# TODO: Check resources sufficient?
# TODO: Process coins.
# TODO: Check transaction successful?
# TODO: Make Coffee.