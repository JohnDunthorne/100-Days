# # hangman
# import random
# print('''
#  __ __   ____  ____    ____  ___ ___   ____  ____  
# |  |  | /    ||    \  /    ||   |   | /    ||    \ 
# |  |  ||  o  ||  _  ||   __|| _   _ ||  o  ||  _  |
# |  _  ||     ||  |  ||  |  ||  \_/  ||     ||  |  |
# |  |  ||  _  ||  |  ||  |_ ||   |   ||  _  ||  |  |
# |  |  ||  |  ||  |  ||     ||   |   ||  |  ||  |  |
# |__|__||__|__||__|__||___,_||___|___||__|__||__|__|
      
# ''')
# word_list = ["apple", "banana", "cherry", "orange", "grape", "kiwi", "melon", "peach", "pear", "plum"]
# chosen_word = random.choice(word_list)
# display = "_" * (len(chosen_word))
# print(display)
# numberoflives = 6
# incorrectlyguessedletters = ""
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
# print(f"{stages[numberoflives]}")
# while numberoflives > 0:

#     while "_" in display:
#         guess = input("Guess a letter: ").lower()

#         newdisplay = ""
#         correctguess = False
#         for i in range(len(chosen_word)):
#             if chosen_word[i] == guess:
#                 newdisplay += guess
#                 correctguess = True
#             else:
#                 newdisplay += display[i]

#         display = newdisplay
#         print(f"your word so far >>>>[        {display}        ]<<<< your word so far")
#         print(f"{stages[numberoflives]}")
#         print(f"Letters you've tried already: {incorrectlyguessedletters}")

#         if not correctguess:
#             if guess not in incorrectlyguessedletters:
#                 incorrectlyguessedletters += guess
#                 numberoflives -= 1
#             else:
#                 print(f"you,ve already tried {guess}")
#             print(f"your word so far >>>>[        {display}        ]<<<< your word so far")
#             print(f"{stages[numberoflives]}")
#             print(f"Letters you've tried already: {incorrectlyguessedletters}")
#         if numberoflives <= 0:
#             break
#     if display == chosen_word:
#         print("Congratulations! You guessed the word:", chosen_word)
#         break
#     else:
#         print("Sorry you ran out of tries")
#         print(f"{stages[numberoflives]}")
#         break

import random

# ASCII art for the hangman
HANGMAN_ASCII = '''
 __ __   ____  ____    ____  ___ ___   ____  ____  
|  |  | /    ||    \  /    ||   |   | /    ||    \ 
|  |  ||  o  ||  _  ||   __|| _   _ ||  o  ||  _  |
|  _  ||     ||  |  ||  |  ||  \_/  ||     ||  |  |
|  |  ||  _  ||  |  ||  |_ ||   |   ||  _  ||  |  |
|  |  ||  |  ||  |  ||     ||   |   ||  |  ||  |  |
|__|__||__|__||__|__||___,_||___|___||__|__||__|__|
'''

# Word list
word_list = ["apple", "banana", "cherry", "orange", "grape", "kiwi", "melon", "peach", "pear", "plum"]

# Choose a random word
chosen_word = random.choice(word_list)
display = "_" * len(chosen_word)
number_of_lives = 6
incorrectly_guessed_letters = set()

# Hangman stages
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(HANGMAN_ASCII)
print(f"Your word so far: {display}")

while number_of_lives > 0:

    guess = input("Guess a letter: ").lower()

    if guess in incorrectly_guessed_letters:
        print(f"You've already tried {guess}")
        continue

    if guess in chosen_word:
        display = ''.join([letter if letter == guess or display[i] != '_' else '_' for i, letter in enumerate(chosen_word)])
    else:
        incorrectly_guessed_letters.add(guess)
        number_of_lives -= 1

    print(f"Your word so far: {display}")
    print(stages[number_of_lives])
    print(f"Letters you've tried already: {', '.join(incorrectly_guessed_letters)}")

    if display == chosen_word:
        print(f"Congratulations! You guessed the word: {chosen_word}")
        break

if number_of_lives <= 0:
    print("Sorry, you ran out of tries.")
    print(stages[number_of_lives])




