# string integer boolean float < these are data types
# int("123") str(123) float(456) float("100.5") < these are ways to type convert
number = round(8/3, 3) # the 3 is the number of decimal places we want
number = (4 // 2) # // gives a floor division, which will return a rounded down int right away, not a float

# Day 2 project tip calculator

total_bill = int(input("What was the total bill? "))
split = int(input("How many people will be paying? "))
tip = int(input("How much of  tip would you like to give as a percentage? "))
total_with_tip = total_bill + (total_bill/100 * tip)
total_for_each = total_with_tip / split
print(round(total_for_each, 2))
