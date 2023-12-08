# blckjack game
import random
import os
import time

print('''

                                  ___           ___           ___         ___          ___           ___           ___     
     _____                       /  /\         /  /\         /__/|       /  /\        /  /\         /  /\         /__/|    
    /  /::\                     /  /::\       /  /:/        |  |:|      /  /:/       /  /::\       /  /:/        |  |:|    
   /  /:/\:\    ___     ___    /  /:/\:\     /  /:/         |  |:|     /__/::\      /  /:/\:\     /  /:/         |  |:|    
  /  /:/~/::\  /__/\   /  /\  /  /:/~/::\   /  /:/  ___   __|  |:|     \__\/\:\    /  /:/~/::\   /  /:/  ___   __|  |:|    
 /__/:/ /:/\:| \  \:\ /  /:/ /__/:/ /:/\:\ /__/:/  /  /\ /__/\_|:|____    \  \:\  /__/:/ /:/\:\ /__/:/  /  /\ /__/\_|:|____
 \  \:\/:/~/:/  \  \:\  /:/  \  \:\/:/__\/ \  \:\ /  /:/ \  \:\/:::::/     \__\:\ \  \:\/:/__\/ \  \:\ /  /:/ \  \:\/:::::/
  \  \::/ /:/    \  \:\/:/    \  \::/       \  \:\  /:/   \  \::/~~~~      /  /:/  \  \::/       \  \:\  /:/   \  \::/~~~~ 
   \  \:\/:/      \  \::/      \  \:\        \  \:\/:/     \  \:\         /__/:/    \  \:\        \  \:\/:/     \  \:\     
    \  \::/        \__\/        \  \:\        \  \::/       \  \:\        \__\/      \  \:\        \  \::/       \  \:\    
     \__\/                       \__\/         \__\/         \__\/                    \__\/         \__\/         \__\/   

      ''')
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")
def dealcard():
    card = random.choice(cards)
    return card
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
replayflag = True
while replayflag == True:

    replayflag = False
    playercards = [dealcard(), dealcard()]
    print(f"your cards are [{playercards}]")
    time.sleep(1)

    computercards = [dealcard(), dealcard()]
    # print(f"player wont see this > {computercards}")
    print(f"The dealer has [{computercards[0]}, ?]")
    time.sleep(1)


    playerscore = sum(playercards)
    computerscore = sum(computercards)

    while playerscore < 21:
        print(f"your current score is {playerscore}")
        choice = input("Do you want to draw another card? press Y on N: ").lower()
        if choice == "y":
            clear_terminal()
            nextplayercard = dealcard()
            playercards.append(nextplayercard)
            playerscore += nextplayercard
            if 11 in playercards and playerscore > 21:
                playerscore -= 10
                playercards[playercards.index(11)] = 1
            print(f"You drew a {nextplayercard}. Your cards: {playercards})")
            if playerscore > 21:
                print(f"you have {playerscore}, sorry you lose")
        elif choice == "n":
            break
        else:
            print("invalid input, please select Y or N: ")

    while computerscore < 17 and playerscore <= 21:
        time.sleep(1)
        print(f"dealer has {computerscore} and must draw another card")
        nextcomputercard = dealcard()
        time.sleep(1)
        print(f"dealer drew {nextcomputercard}")
        computercards.append(nextcomputercard)
        computerscore += nextcomputercard

    if computerscore > 21 and playerscore <= 21:
        print(f"dealer has {computerscore}, you win")

    elif computerscore <= 21 and playerscore <= 21:
        if playerscore > computerscore:
            print(f"you have {playerscore} and dealer has {computerscore} you win!")
        elif computerscore > playerscore:
            print(f"you have {playerscore} and dealer has {computerscore} you lose!")
        else:
            print(f"you have {playerscore} and dealer has {computerscore} its a draw!")

    
    while replayflag == False:
        replay = input("would you like to play again? Y or N: ").lower()
        if replay == "y":
            replayflag = True
            clear_terminal()
        elif replay == "n":
            clear_terminal()
            print('''       _                 _          
   _  | |               | |         
 _| |_| |__  _____ ____ | |  _  ___ 
(_   _)  _ \(____ |  _ \| |_/ )/___)
  | |_| | | / ___ | | | |  _ (|___ |
   \__)_| |_\_____|_| |_|_| \_|___/ 
                                    
    ___                             
   / __)                            
 _| |__ ___   ____                  
(_   __) _ \ / ___)                 
  | | | |_| | |                     
  |_|  \___/|_|                     
                                    
       _              _             
      | |            (_)            
 ____ | | _____ _   _ _ ____   ____ 
|  _ \| |(____ | | | | |  _ \ / _  |
| |_| | |/ ___ | |_| | | | | ( (_| |
|  __/ \_)_____|\__  |_|_| |_|\___ |
|_|            (____/        (_____|
                  
                  
                  ''')
            break
        else:
            print("invalid input, please type Y or N: ")

            


