# hangman
import random

word_list = ["apple", "banana", "cherry", "orange", "grape", "kiwi", "melon", "peach", "pear", "plum"]
chosen_word = random.choice(word_list)

print(chosen_word)
display = "_ " * (len(chosen_word))
print(display)

guess = input("Guess a letter: ").lower()

display = ""

for letter in chosen_word:
    if letter == guess:
        display += f"{letter}"
    elif letter != guess:
        display += f"_ "

print(display)
