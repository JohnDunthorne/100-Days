# hangman
import random

word_list = ["apple", "banana", "cherry", "orange", "grape", "kiwi", "melon", "peach", "pear", "plum"]
random_number = random.randint(0, len(word_list) -1)

chosen_word = word_list[random_number]

print(chosen_word)

guess = input("Guess a letter: ")
guess_lowercase = guess.lower()

if guess_lowercase in chosen_word:
    print(f"You guessed one of the letters")
else:
    print(f"this letter is not in the word")
