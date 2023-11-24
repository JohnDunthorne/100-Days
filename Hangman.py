import random
import os
import msvcrt  # Import the msvcrt module for Windows-specific input


def print_centered(message, width=80):
    print(message.center(width))


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


clear_terminal()
print_centered(
    """
                  Welcome to:
 __ __   ____  ____    ____  ___ ___   ____  ____  
|  |  | /    ||    \  /    ||   |   | /    ||    \ 
|  |  ||  o  ||  _  ||   __|| _   _ ||  o  ||  _  |
|  _  ||     ||  |  ||  |  ||  \_/  ||     ||  |  |
|  |  ||  _  ||  |  ||  |_ ||   |   ||  _  ||  |  |
|  |  ||  |  ||  |  ||     ||   |   ||  |  ||  |  |
|__|__||__|__||__|__||___,_||___|___||__|__||__|__|
      
              Press Enter to play
      
"""
)
input("")

clear_terminal()
# fmt: off
word_list = [
    "apple", "banana", "orange", "table", "chair", "house", "car", "cat", "dog", "bird",
    "sun", "moon", "star", "water", "tree", "forest", "mountain", "river", "ocean",
    "book", "pen", "paper", "computer", "phone", "music", "movie", "friend", "family", "love",
    "happy", "sad", "laugh", "cry", "walk", "run", "jump", "swim", "eat", "drink",
    "sleep", "dream", "work", "play", "learn", "teach", "school", "college", "university",
    "job", "money", "time", "day", "night", "morning", "evening", "week", "month", "year",
    "today", "tomorrow", "yesterday", "red", "blue", "green", "yellow", "white", "black",
    "gray", "color", "number", "letter", "word", "sentence", "paragraph", "story", "picture",
    "art", "science", "math", "history", "geography", "language", "music", "sport", "game",
    "play", "watch", "listen", "talk", "speak", "hear", "see", "touch", "feel", "taste", "smell",
    "hot", "cold", "big", "small"
]
# fmt: on

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
ENDC = "\033[0m"

chosen_word = random.choice(word_list)
display = "_" * len(chosen_word)

print(f"Your word is this long: {BLUE}{' '.join(display)}{ENDC}")

number_of_lives = 6
incorrectly_guessed_letters = ""
stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

print(f"{stages[number_of_lives]}")

while number_of_lives > 0:
    while "_" in display:
        print("Guess a letter!")
        guess = msvcrt.getwch().lower()  # Use msvcrt.getwch() for single-key input
        clear_terminal()
        new_display = ""
        correct_guess = False

        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                new_display += guess
                correct_guess = True
            else:
                new_display += display[i]

        display = new_display

        if not correct_guess:
            if guess not in incorrectly_guessed_letters:
                incorrectly_guessed_letters += guess
                number_of_lives -= 1
            else:
                print(RED + f"You've already tried {guess}" + ENDC)

        if number_of_lives <= 0:
            break

        print("")
        print(f"Your word so far: {BLUE}{' '.join(display)}{ENDC}")
        print(f"{stages[number_of_lives]}")
        print(
            f"Letters you've tried already: {YELLOW}{' '.join(incorrectly_guessed_letters)}{ENDC}"
        )
        print("")

    if "_" not in display:
        print(GREEN + f"Congratulations! You guessed the word: {chosen_word}" + ENDC)
        break
    else:
        print(RED + f"Sorry, you ran out of tries. The word was {chosen_word}" + ENDC)
        print(f"{stages[number_of_lives]}")
        break
