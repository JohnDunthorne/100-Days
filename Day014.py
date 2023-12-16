import Day014Art
from Day014Data import data
from random import randint

print(Day014Art.logo)
print("Guess who has a larger social media following!")

# pull a random starting person
# keys are - 'name''follower_count''description''country'
randomindex = randint(0, len(data) - 1)
print(len(data))
print(f"{data[randomindex]['name']} is a {data[randomindex]['description']} from {data[randomindex]['country']}")

print(Day014Art.vs)
# pull a random secondary person

# ask for higher or lower

# comapre result

# if correct make seconady person first person

# generate new seconday person

# increment score

# game over if wrong