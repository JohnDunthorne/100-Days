# hangman
import random

word_list = ["apple", "banana", "cherry", "orange", "grape", "kiwi", "melon", "peach", "pear", "plum"]
chosen_word = random.choice(word_list)
print(chosen_word)
display = "_" * (len(chosen_word))
print(display)
numberoflives = 5
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
        print(display)

        if not correctguess:
            numberoflives -= 1
            print(f"sorry {guess} is not in the word you have {numberoflives} tries left")
        if numberoflives <= 0:
            break
    if display == chosen_word:
        print("Congratulations! You guessed the word:", chosen_word)
        break
    else:
        print("Sorry you ran out of tries")
        break



