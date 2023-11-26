# Dictionaries, they should be formatted like this:
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

# This code below will print the definition of bug, you use the key to print the value it is paired with.
print(programming_dictionary["Bug"])

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
for student in student_scores:
    score = student_scores[student] # this is replacing 'student' with whoever its currently looping through
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] =  "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)