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
    string = (f"{data[randomindex]['name']} is a {data[randomindex]['description']} from {data[randomindex]['country']}")
    followers = data[randomindex]['follower_count']
    return string, followers


def guess(celeb1followers, celeb2followers):
    selection = input("Who do you think has a larger following 1, or 2? ")
    if (selection == '1' and celeb1followers > celeb2followers) or (selection == '2' and celeb2followers > celeb1followers):
        return True
    else:
        return False
    
def new_celebs():
    global celeb1, celeb1followers, celeb2, celeb2followers
    celeb1, celeb1followers = celeb2, celeb2followers
    celeb2, celeb2followers = random_person()

    
    

# Choose the two celebrities
celeb1, celeb1followers = (random_person())
celeb2, celeb2followers = (random_person())

# show the initial matchup
print(celeb1)
print(celeb1followers)

# Print the vs logo
print(Day014Art.vs)

print(celeb2)
print(celeb2followers)
score = 0
while True:
    if guess(celeb1followers, celeb2followers) == True:
        print("Correct")
        score += 1
        print(f"Your score is {score}")
        new_celebs()
    else:
        print(f"Sorry thats wrong, your final score was {score}")
        break

