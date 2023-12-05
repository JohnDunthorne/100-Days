# guess the number game
import random

def select_difficulty():
    difficulty_selection = input("Select a difficulty: type 'easy' or 'hard'\n").lower()
    if difficulty_selection == "easy":
        lives = 10
        return lives
    elif difficulty_selection == "hard":
        lives = 5
        return lives
    else:
        return select_difficulty()
    
    
def guess():
    global lives
    while lives > 0:
        print(f"you have {lives} tries left")
        guess = int(input("Make a guess: "))
        if guess > number_to_guess:
            print("your guess is too high")
            lives -= 1
        elif guess < number_to_guess:
            print("your guess is too low")
            lives -= 1
        else:
            print("you answered correctly")
            break
    else:
        print(f"sorry you ran out of lives, the number was {number_to_guess}")
        

continue_play = True
while continue_play:
    number_to_guess = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100")
    lives = select_difficulty()

    guess()

    play_again = input("would you like to play again?: Y or N: ").lower()
    if play_again == "y":
        continue_play = True
    elif play_again == "n":
        print("Thanks for playing")
        continue_play = False
    else:
        print("invalid input")

        #loop through this last part
        z
       






