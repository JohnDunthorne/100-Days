# there are 3 types of functions, plain, functions with inputs and functions with outputs.

def formattedname(f_name, l_name):
    ff_name = f_name.title()
    fl_name = l_name.title()
    return f"{ff_name} {fl_name}"

f_name = input("please type your first name: ")
l_name = input("please type you last name: ")

titled_name = formattedname(f_name, l_name)
print(titled_name)