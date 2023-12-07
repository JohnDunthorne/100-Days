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


# #🚨 Do NOT change any of the code bel 
# year = int(input()) # Enter a year
# month = int(input()) # Enter a month
# days = days_in_month(year, month)
# print(days)

# Calculator program


# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# operations = {
#     "+" : add,
#     "-" : subtract,
#     "*" : multiply,
#     "/" : divide
#     }

# num1 = float(input("Select first number: "))
# num2 = float(input("Select second number: "))
# for operator in operations:
#     print(operator)
# operation_selection = input("Type an operator from the selection above: ")
# operator = operations[operation_selection]
# result = operator(num1, num2)
# print(f"{num1} {operation_selection} {num2} = {result}")


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

continue_flag = True

while continue_flag:
    num1 = float(input("Select the first number: "))
    num2 = float(input("Select the second number: "))

    for operator in operations:
        print(operator)

    operation_selection = input("Type an operator from the selection above: ")
    if operation_selection in operations:
        operator = operations[operation_selection]
        result = operator(num1, num2)
        print(f"{num1} {operation_selection} {num2} = {result}")

        while True:
            continue_operation = input(
                "Do you want to continue with the result? (yes/no): "
            ).lower()
            if continue_operation == "yes":
                old_result = result  # Store the old result
                new_num = float(input("Enter a new number: "))
                for new_operator in operations:
                    print(new_operator)
                new_operation_selection = input(
                    "Type an operator from the selection above: "
                )

                if new_operation_selection in operations:
                    new_operator = operations[new_operation_selection]
                    result = new_operator(
                        old_result, new_num
                    )  # Use the old result in the new operation
                    print(
                        f"{old_result} {new_operation_selection} {new_num} = {result}"
                    )
                else:
                    print(
                        "Invalid operator. Please choose from the available operators."
                    )

            elif continue_operation == "no":
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    else:
        print("Invalid operator.")

    continue_program = input(
        "Do you want to continue with the program? (yes/no): "
    ).lower()
    if continue_program != "yes":
        continue_flag = False
