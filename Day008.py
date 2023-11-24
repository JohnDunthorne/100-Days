

def greet(name, birthday, age): # name is the parameter, parameters expect arguments when function is called
    print("hi")
    print(name)
    print(f"your birthday is on {birthday} that makes you {age}")

my_name = "John"
my_birthday = "11/17/80"
my_age = 43
greet(my_name, my_birthday, my_age) # when calling a function that has parameters, arguments are expected, these can use variables or hard coded data
# note that the arguments name does not have to match the paramenter name, but whatever is in the parentheses will be used as the argument.