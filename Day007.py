# hangman
import random
print('''
      






 __ __   ____  ____    ____  ___ ___   ____  ____  
|  |  | /    ||    \  /    ||   |   | /    ||    \ 
|  |  ||  o  ||  _  ||   __|| _   _ ||  o  ||  _  |
|  _  ||     ||  |  ||  |  ||  \_/  ||     ||  |  |
|  |  ||  _  ||  |  ||  |_ ||   |   ||  _  ||  |  |
|  |  ||  |  ||  |  ||     ||   |   ||  |  ||  |  |
|__|__||__|__||__|__||___,_||___|___||__|__||__|__|
      
''')
word_list = ["apple", "banana", "cherry", "orange", "grape", "kiwi", "melon", "peach", "pear", "plum"]
chosen_word = random.choice(word_list)
display = "_" * (len(chosen_word))
print(display)
numberoflives = 6
incorrectlyguessedletters = ""
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
print(f"{stages[numberoflives]}")
while numberoflives > 0:

    while "_" in display:
        guess = input("Guess a letter: ").lower()

        newdisplay = ""
        correctguess = False
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                newdisplay += guess
                correctguess = True
            else:
                newdisplay += display[i]

        display = newdisplay
        print(f"your word so far >>>>[        {display}        ]<<<< your word so far")
        print(f"{stages[numberoflives]}")
        print(f"\nLetters you've tried already: {incorrectlyguessedletters}\n\n\n\n\n\n")

        if not correctguess:
            if guess not in incorrectlyguessedletters:
                incorrectlyguessedletters += guess
                numberoflives -= 1
            print(f">>>>[{display}]<<<<")
            print(f"{stages[numberoflives]}")
            print(f"\n Letters you've tried already: {incorrectlyguessedletters}\n\n\n\n\n\n")
        if numberoflives <= 0:
            break
    if display == chosen_word:
        print("\n\n\n\n\n\n\n\n\n\nCongratulations! You guessed the word:", chosen_word)
        break
    else:
        print("\n\n\n\n\n\n\nSorry you ran out of tries")
        print(f"{stages[numberoflives]}\n\n\n\n\n\n")
        break



