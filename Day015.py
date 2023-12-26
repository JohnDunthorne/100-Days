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

continue_coffee_machine = True

while continue_coffee_machine:
    while True:
        choice = input(f"“What would you like? (espresso/latte/cappuccino):”\n").lower()
        if choice in MENU:
            # Check and deduct resources for water
            if 'water' in MENU[choice]['ingredients']:
                water_needed = MENU[choice]['ingredients']['water']
                if water_left >= water_needed:
                    water_left -= water_needed
                else:
                    print("Sorry, not enough water. Please choose another drink.")
                    continue

            # Check and deduct resources for milk
            if 'milk' in MENU[choice]['ingredients']:
                milk_needed = MENU[choice]['ingredients']['milk']
                if milk_left >= milk_needed:
                    milk_left -= milk_needed
                else:
                    print("Sorry, not enough milk. Please choose another drink.")
                    continue

            # Check and deduct resources for coffee
            if 'coffee' in MENU[choice]['ingredients']:
                coffee_needed = MENU[choice]['ingredients']['coffee']
                if coffee_left >= coffee_needed:
                    coffee_left -= coffee_needed
                else:
                    print("Sorry, not enough coffee. Please choose another drink.")
                    continue

            # If all ingredients are available, print a message indicating the drink is being made
            print(f"resources deducted")
            break
        elif choice == 'off':
            exit()
        elif choice == 'report':
            print(f"water = {water_left}\n"
                  f"milk = {milk_left}\n"
                  f"coffee = {coffee_left}")
        else:
            print("invalid input")

    print(f"water = {water_left}\n"
          f"milk = {milk_left}\n"
          f"coffee = {coffee_left}")
    if choice in MENU:
        print(f"You chose {choice} It costs ${MENU[choice]['cost']:.2f}")

    cost = MENU[choice]['cost']
    number_of_pennies = int(input("how many pennies will you deposit: "))
    number_of_nickles = int(input("how many nickles will you deposit: "))
    number_of_dimes = int(input("how many dimes will you deposit: "))
    number_of_quarters = int(input("how many quarters will you deposit: "))
    total_money = (number_of_pennies * 0.01) + \
                  (number_of_nickles * 0.05) + \
                  (number_of_dimes * 0.10) + \
                  (number_of_quarters * 0.25)
    print(total_money)
    if total_money >= cost:
        change = total_money - cost
        print(f"Enjoy your drink your change is {change:.2f}")
    elif total_money < cost:
        print(f"Sorry that's not enough money, here's your ${total_money:.2f} back")

    continue_making = input("would you like to make another coffee Y or N: ").lower()
    if continue_making == 'y':
        continue_coffee_machine = True
    else:
        continue_coffee_machine = False


