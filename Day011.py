# blckjack game
import random

def dealcard():
    card = random.choice(cards)
    return card
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

playercard1 = dealcard()
playercard2 = dealcard()
print(f"your cards are [{playercard1}, {playercard2}]")