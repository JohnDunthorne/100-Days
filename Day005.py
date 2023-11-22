# # for loops
# fruits = ["apple", "pear", "peach"]
# for fruit in fruits:
#     print(fruit)

# random password generator

import random

# fmt: off
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# fmt: on

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

randomletters = ""
for item in range(nr_letters):
    listlength = len(letters)
    randomint = random.randint(0, listlength - 1)
    randomletters += letters[randomint]

randomsymbols = ""
for item in range(nr_symbols):
    listlength = len(symbols)
    randomint = random.randint(0, listlength - 1)
    randomsymbols += symbols[randomint]

randomnumbers = ""
for item in range(nr_numbers):
    listlength = len(numbers)
    randomint = random.randint(0, listlength - 1)
    randomnumbers += numbers[randomint]

combined_chars = list(randomletters + randomnumbers + randomsymbols)

random.shuffle(combined_chars)

randomstring = "".join(combined_chars)

print(randomstring)
