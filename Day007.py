# hangman
import random
import os
import sys

def play_again():
    play_again = input("Would you like to play again? Y or N: \n").lower()
    while play_again != "y" and play_again != "n":
        print("Invalid input. Please enter Y or N.")
        play_again = input("Would you like to play again? Y or N: \n").lower()

    if play_again == "y":
        main()

    elif play_again == "n":
        print("Thank you for playing. See you!")
        sys.exit()
def main():
    def print_centered(message, width=80):
        print(message.center(width))


    def clear_terminal():
        os.system("cls" if os.name == "nt" else "clear") if os.name == "nt" else "clear"


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
        'amazing', 'attention', 'beautiful', 'business',
        'celebrate', 'creative', 'decision', 'delicate', 'discover',
        'education', 'effort', 'elephant', 'entertain', 'excellent',
        'fascinating', 'foundation', 'fortunate', 'freedom', 'fulfill',
        'generate', 'gigantic', 'grateful', 'growth', 'guidance',
        'harmony', 'historic', 'imagination', 'incredible', 'inspire',
        'jubilant', 'journey', 'justice',
        'knowledge', 'landscape', 'laughter', 'leadership', 'limitless',
        'magnificent', 'momentum', 'motivation',
        'navigate', 'nostalgia',
        'opportunity', 'optimistic', 'organization', 'outstanding',
        'passionate', 'perseverance', 'positive', 'prosperity', 'purposeful',
        'quality', 'quantum', 'quest',
        'radiant', 'resilience', 'revolutionary', 'satisfaction', 'serenity',
        'simplicity', 'sparkle', 'spectacular', 'success', 'synergy',
        'transform', 'triumphant', 'trustworthy',
        'universe', 'unstoppable', 'uplifting',
        'vibrant', 'victory', 'visionary', 'vivacious',
        'wonderful', 'wholesome',
        'xylophone', 'xenon', 'xerox', 'xenophobia', 'xenolithic',
        'yielding', 'yearning', 'yesterday',
        'zealous', 'zenith', 'zigzag', 'zoology', 'zephyr'
    ]
    # fmt: on
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    ENDC = "\033[0m"
    chosen_word = random.choice(word_list)
    display = "_" * (len(chosen_word))
    print("")
    print(f"Your word is this long: ", end="")
    print(BLUE + " ".join(display) + ENDC)
    numberoflives = 6
    incorrectlyguessedletters = ""
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
    print(f"{stages[numberoflives]}")
    while numberoflives > 0:
        while "_" in display:
            guess = input("Guess a letter: ").lower()
            clear_terminal()
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
                    print(RED + f"you've already tried {guess}" + ENDC)

            if numberoflives <= 0:
                break
            print("")
            print(f"your word so far: ", end="")
            print(BLUE + " ".join(display) + ENDC)
            print(f"{stages[numberoflives]}")
            print(f"Letters you've tried already: ", end="")
            print(YELLOW + " ".join(incorrectlyguessedletters) + ENDC)
            print("")
        if display == chosen_word:
            print(GREEN + "Congratulations! You guessed the word:", chosen_word + ENDC)
            play_again()
        else:
            print(RED + f"Sorry you ran out of tries the word was {chosen_word}" + ENDC)
            print(f"{stages[numberoflives]}")
            play_again()

main()
