# there are 3 types of functions, plain, functions with inputs and functions with outputs.

# def formattedname(f_name, l_name):
#     ff_name = f_name.title()
#     fl_name = l_name.title()
#     return f"{ff_name} {fl_name}"

# f_name = input("please type your first name: ")
# l_name = input("please type you last name: ")

# titled_name = formattedname(f_name, l_name)
# print(titled_name)


# this code below was the challenge to find how how many days there were in a month depending on the year
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False
  
# # TODO: Add more code here 👇
# def days_in_month(p_year, p_month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if is_leap(p_year) == True:
#     if p_month == 2:
#       return 29
#     else:
#       return month_days[p_month -1]
#   else:
#     return month_days[p_month -1]  


  
# #🚨 Do NOT change any of the code below 
# year = int(input()) # Enter a year
# month = int(input()) # Enter a month
# days = days_in_month(year, month)
# print(days)