import Day014Art
from Day014Data import data
from random import randint

# Show the name of the game and description of the game
print(Day014Art.logo)
print("Guess who has a larger social media following!")

# keys are - 'name''follower_count''description''country'

#generate a random person

def random_person():
    randomindex = randint(0, len(data) - 1)
    return (f"{data[randomindex]['name']} is a {data[randomindex]['description']} from {data[randomindex]['country']}")


celeb1 = (random_person())
celeb2 = (random_person())

print(celeb1)
print(celeb2)
print(celeb1)





# # Print the vs logo
# print(Day014Art.vs)

# # pull a random secondary person
# randomindex2 = randint(0, len(data) - 1)
# print(f"{data[randomindex2]['name']} is a {data[randomindex2]['description']} from {data[randomindex2]['country']}")

# # ask for higher or lower
# follower_count_1 = data[randomindex1]['follower_count']
# follower_count_2 = data[randomindex2]['follower_count']
# guess = input("Who has a higher following, type 1 or 2 ")

# # comapre result
# score = 0
# if guess == "1":
#     if follower_count_1 > follower_count_2:
#         print("Correct")
#         score += 1
#         print(f"your current score is {score}")
#     else:
#         print("sorry thats wrong")
# if guess == "2":
#     if follower_count_2 > follower_count_1:
#         print("Correct")
#         score += 1
#         print(f"your current score is {score}")
#     else:
#         print("sorry thats wrong")

# while score > 0:
#     randomindex2 = randomindex1
#     print(randomindex1)
#     newrandomindex = randint(0, len(data) - 1)
#     print(f"{data[newrandomindex]['name']} is a {data[newrandomindex]['description']} from {data[newrandomindex]['country']}")
# # generate new seconday person

# # increment score

# # game over if wrong