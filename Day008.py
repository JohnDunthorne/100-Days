# passing arguments through functions
# potitional arguements
# keyword arguements


def greet(
    name, birthday, age
):  # name is the parameter, parameters expect arguments when function is called
    print("hi")
    print(name)
    print(f"your birthday is on {birthday} that makes you {age}")


my_name = "John"
my_birthday = "11/17/80"
my_age = 43
# greet(my_name, my_birthday, my_age) # when calling a function that has parameters, arguments are expected, these can use variables or hard coded data
# note that the arguments name does not have to match the paramenter name, but whatever is in the parentheses will be used as the argument.

# The above are referred to as positional arguements, as the order they are type in is important, name must be first then birthday, then age
# is i mixed these up they would print out in the wrong order, hence positional

# greet(birthday=my_birthday, age=my_age, name=my_name) #when doing key pairs like this, avoid spaces while assigning, good practice.

# above is the other version of arguments called keyword arguments, i take the name of the parameter, then assign the argument to it
# i can now assign all my arguments to the parameters names in any order i wish.
# as you can see above the argments are not in the correct order, but are paired with the parameter names.

# paint coverage function
# import math

# def paint_calc(height, width, cover):
#   cans = math.ceil((height*width)/cover)
#   print(f"You'll need {cans} cans of paint.")

# test_h = 4
# test_w = 5
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# Ceasar cipher

import sys


def caesar(p_text, p_shift, p_direction):
    shifted_word = ""
    for letter in p_text:
        if letter.isalpha():
            index = alphabet.index(letter)
            if p_direction == "e":
                new_index = (index + p_shift) % 26
            elif p_direction == "d":
                new_index = (index - p_shift) % 26
            shifted_letter = alphabet[new_index]
            shifted_word += shifted_letter
        else:
            shifted_word += letter
    print(f"your shuffled word is {shifted_word}")


def main():
    direction = input("To encode type 'E' and to decode type 'D':\n").lower()
    while direction != "d" and direction != "e":
        direction = input("To encode type 'E' and to decode type 'D':\n").lower()
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)
        answer = input(
            "would you like to try again? press Y for yes an N for no:\n"
        ).lower()
        retry(answer)


def retry(answer):
    while answer != "n" and answer != "y":
        answer = input("would you like to try again? press Y for yes an N for no:\n")
    else:
        if answer == "y":
            main()
        elif answer == "n":
            sys.exit()


alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

print(
    """
 ________  ________  _______   ________  ________  ________       
|\   ____\|\   __  \|\  ___ \ |\   ____\|\   __  \|\   __  \    
\ \  \___|\ \  \|\  \ \   __/|\ \  \___|\ \  \|\  \ \  \|\  \   
 \ \  \    \ \   __  \ \  \_|/_\ \_____  \ \   __  \ \   _  _\  
  \ \  \____\ \  \ \  \ \  \_|\ \|____|\  \ \  \ \  \ \  \\\  \| 
   \ \_______\ \__\ \__\ \_______\____\_\  \ \__\ \__\ \__\\\ _\ 
    \|_______|\|__|\|__|\|_______|\_________\|__|\|__|\|__|\|__|
                                 \|_________|                   
                                                                
                                                                
 ________  ___  ________  ___  ___  _______   ________          
|\   ____\|\  \|\   __  \|\  \|\  \|\  ___ \ |\   __  \         
\ \  \___|\ \  \ \  \|\  \ \  \\ \\  \ \   __/|\ \  \|\  \        
 \ \  \    \ \  \ \   ____\ \   __  \ \  \_|/_\ \   _  _\       
  \ \  \____\ \  \ \  \___|\ \  \ \  \ \  \_|\ \ \  \\\  \|      
   \ \_______\ \__\ \__\    \ \__\ \__\ \_______\ \__\\\ _\      
    \|_______|\|__|\|__|     \|__|\|__|\|_______|\|__|\|__|
      """
)

main()
