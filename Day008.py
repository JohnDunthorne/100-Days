# passing arguments through functions
# potitional arguements
# keyword arguements

def greet(name, birthday, age): # name is the parameter, parameters expect arguments when function is called
    print("hi")
    print(name)
    print(f"your birthday is on {birthday} that makes you {age}")

my_name = "John"
my_birthday = "11/17/80"
my_age = 43
greet(my_name, my_birthday, my_age) # when calling a function that has parameters, arguments are expected, these can use variables or hard coded data
# note that the arguments name does not have to match the paramenter name, but whatever is in the parentheses will be used as the argument.

# The above are referred to as positional arguements, as the order they are type in is important, name must be first then birthday, then age
# is i mixed these up they would print out in the wrong order, hence positional

greet(birthday=my_birthday, age=my_age, name=my_name) #when doing key pairs like this, avoid spaces while assigning, good practice.

# above is the other version of arguments called keyword arguments, i take the name of the parameter, then assign the argument to it
# i can now assign all my arguments to the parameters names in any order i wish.
# as you can see above the argments are not in the correct order, but are paired with the parameter names.

# Write your code below this line 👇
import math

def paint_calc(height, width, cover):
  cans = math.ceil((height*width)/cover)
  print(f"You'll need {cans} cans of paint.")



# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = 4
test_w = 5
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)