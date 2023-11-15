# Comparison operators
# > greater than
# >= greater than or equal to
# < less than
# <= less than or equal to
# == equal to
# != not equal to

# # Which year do you want to check?
# year = 2100

# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# if (year % 4 == 0 or year % 400 == 0) and not year % 100 == 0:
#     print("Leap year")
# else:
#     print("Not leap year")


# print("Thank you for choosing Python Pizza Deliveries!")
# size = input(
#     "What size pizza do you want? S, M, or L"
# )  # What size pizza do you want? S, M, or L
# add_pepperoni = input("Do you want pepperoni? Y or N")  # Do you want pepperoni? Y or N
# extra_cheese = input(
#     "Do you want extra cheese? Y or N"
# )  # Do you want extra cheese? Y or N
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
# if add_pepperoni == "Y" and size == "S":
#     bill += 2
# elif add_pepperoni == "N":
#     bill += 0
# else:
#     bill += 3
# if extra_cheese == "Y":
#     bill += 1
# else:
#     bill += 0

# print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is: ${bill}.")


# Love calculator
# name1 = "Brad Pitt"
# name2 = "Jennifer Aniston"
# both_names = name1 + name2
# name_true = ""
# name_love = ""
# for letter in both_names:
#     if letter.lower() in ["t", "r", "u", "e"]:
#         name_true += letter
# for letter in both_names:
#     if letter.lower() in ["l", "o", "v", "e"]:
#         name_love += letter
# name_true_digit = len(name_true)
# name_love_digit = len(name_love)
# score = int(f"{name_true_digit}{name_love_digit}")
# print(f"Your score is {score}", end="")
# if score < 10 or score > 90:
#     print(", you go together like coke and mentos.")
# elif score >= 40 and score <= 50:
#     print(", you are alright together.")
# else:
#     print(".")
