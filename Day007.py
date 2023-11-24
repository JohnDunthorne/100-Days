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

        if not correctguess:
            if guess not in incorrectlyguessedletters:
                incorrectlyguessedletters += guess
                numberoflives -= 1
            else:
                print(f"you,ve already tried {guess}")
            
        if numberoflives <= 0:
            break
        print("")
        print(f"your word so far: {display}")
        print(f"{stages[numberoflives]}")
        print(f"Letters you've tried already: {incorrectlyguessedletters}")
        print("")
    if display == chosen_word:
        print("Congratulations! You guessed the word:", chosen_word)
        break
    else:
        print("Sorry you ran out of tries")
        print(f"{stages[numberoflives]}")
        break