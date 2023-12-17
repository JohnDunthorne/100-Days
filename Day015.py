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

# TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”


def user_choice():
    return input(f"What kind of coffe would you like?\n"
                 f"espresso which costs {MENU['espresso']['cost']}\n"
                 f"latte which costs {MENU['latte']['cost']}\n"
                 f"cappuccino which costs {MENU['cappuccino']['cost']}\n"
                 f"Type 'E' for an espresso, 'L' for latte and 'C' for cappuccino:\n").lower()


def check_resources(selection):
    if selection == 'e':
        water_left = resources['water'] - MENU['espresso']['ingredients']['water']
        coffee_left = resources['coffee'] - MENU['espresso']['ingredients']['coffee']
        
        print(f"you have {water_left} water left")
        print(f"you have {milk_left} water left")
        print(f"you have {coffee_left} water left")


# TODO: Turn off the Coffee Machine by entering “off” to the prompt
# TODO: Print report.

while True:
    choice = user_choice()
    if choice == 'off':
        exit()
    elif choice == "report":
        print(resources)
    elif choice == 'e':
        print("selected e")
        check_resources(choice)
    elif choice == 'l':
        print("selected l")
    elif choice == 'c':
        print("selected c")
    else:
        print("invalid input, must type 'report', 'e', 'l', 'c', or 'off' to turn off the machine.")

    # TODO: Check resources sufficient?
# TODO: Process coins.
# TODO: Check transaction successful?
# TODO: Make Coffee.
