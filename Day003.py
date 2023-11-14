# Comparison operators
# > greater than
# >= greater than or equal to
# < less than
# <= less than or equal to
# == equal to
# != not equal to

# Which year do you want to check?
year = 2100

# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if (year % 4 == 0 or year % 400 == 0) and not year % 100 == 0:
    print("Leap year")
else:
    print("Not leap year")


print("Thank you for choosing Python Pizza Deliveries!")
size = input("")  # What size pizza do you want? S, M, or L
add_pepperoni = input("")  # Do you want pepperoni? Y or N
extra_cheese = input("")  # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill = 0
if size == S:
    bill += 15
