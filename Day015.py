# Using pycharm environment
# installed
# coffee machine

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
choice = input(f"What kind of coffe would you like?\n"
               f"espresso which costs {MENU['espresso']['cost']}\n"
               f"latte which costs {MENU['latte']['cost']}\n"
               f"cappuccino which costs {MENU['cappuccino']['cost']}")
# TODO: Turn off the Coffee Machine by entering “off” to the prompt
# TODO: Print report.
# TODO: Check resources sufficient?
# TODO: Process coins.
# TODO: Check transaction successful?
# TODO: Make Coffee.
