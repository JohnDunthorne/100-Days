import random

# # to use the random module you can use for example random.randint(1, 10) for whole numbers, random.random() for a float between 0 and 1

# heads_or_tails = random.randint(1, 2)
# if heads_or_tails == 1:
#     print("Heads")
# else:
#     print("Tails")

# # nested lists
# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = ["a", "b", "c", "d", "e", "f", "g"]

# list3 = [list1, list2]
# print(f"{list1}\n{list2}\n{list3}")

# rock paper scissors game
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
user_choice = int(input("What's your choice? 0 = rock, 1 = paper, 2 = scissors\n"))
computer_choice = random.randint(0, 2)

print("You Chose\n")
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
else:
    print(scissors)

print("\nComputer Chose\n")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

print("")

if user_choice == computer_choice:
    print("There was a draw")
elif (
    (user_choice == 0 and computer_choice == 2)
    or (user_choice == 1 and computer_choice == 0)
    or (user_choice == 2 and computer_choice == 1)
):
    print("You Win")
else:
    print("You lose")
