# hangman
import random

word_list = ["apple", "banana", "cherry", "orange", "grape", "kiwi", "melon", "peach", "pear", "plum"]
chosen_word = random.choice(word_list)

print(chosen_word)

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print(f"{letter} ", end="")
    else:
        print(f"_ ", end="")
