# Dictionaries, they should be formatted like this:
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again.",
# }

# This code below will print the definition of bug, you use the key to print the value it is paired with.
# print(programming_dictionary["Bug"])

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,

# 🚨 Don't change the code above 👆
# : Create an empty dictionary called student_grades.
# student_grades = {}
# for student in student_scores:
#     score = student_scores[student] # this is replacing 'student' with whoever its currently looping through
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"

# for student, score in student_scores.items(): # this is better than above as it deals with the key value pair separately to begin with
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"

# print(student_grades)

# appending a dictionary inside a travel log list, with a function

# country = input() # Add country name
# visits = int(input()) # Number of visits
# list_of_cities = eval(input()) # create list from formatted string

# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]
# # Do NOT change the code above 👆

# # Write the function that will allow new countries
# # to be added to the travel_log. 
# def add_new_country(country, visits, list_of_cities):
#   added_coutry = {"country" : country, "visits" : visits, "cities" : list_of_cities}
#   travel_log.append(added_coutry)
# # Do not change the code below 👇
# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")



# alternative

# def add_new_country(name, times_visited, cities_visited): # the parameters for the arguements, they are named differently but are positional
#   new_country = {}
#   new_country["country"] = name
#   new_country["visits"] = times_visited
#   new_country["cities"] = cities_visited
#   travel_log.append(new_country)

# add_new_country(country, visits, list_of_cities) # here are the positional arguments
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")

# this way we added the key value pairs to a dictionary one by one, and then appended it to the travel log

# silent auction
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear") if os.name == "nt" else "clear"

def add_details():
    global bid_dict
    name = input("What is your name? ")
    bid = float(input("How much would you like to bid? $"))
    bid_dict.append ({"name": name, "bid": bid})

print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\)
      ''')
bid_dict = []
add_details()
anotherbidder = input("Is there another bidder? Y on N: ").lower()
while anotherbidder == "y":
    clear_screen()
    add_details()
    anotherbidder = input("Is there another bidder? Y on N: ").lower()
else:
    highest_bidder_name = ""
    highest_bid = 0.0

    # Loop through the list of bidders
    for bidder in bid_dict:
        name = bidder['name']
        bid = bidder['bid']

        # Check if the current bid is higher than the previous highest bid
        if bid > highest_bid:
            highest_bidder_name = name
            highest_bid = int(bid)

    # Print the result
    if highest_bidder_name:
        print(f"The bidder with the highest bid is {highest_bidder_name} with a bid of ${highest_bid}.")
    else:
        print("There are no bidders.") 

