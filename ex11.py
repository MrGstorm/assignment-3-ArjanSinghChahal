###############################################################################
#  Program Name   : ex11.py
#  Author         : Arjan Singh Chahal
#  Task           : Program asks user for name and age and prints a sentances
#                   about them using that information
###############################################################################


def print_info(name, age):
    print(f"My name is {name} and I am {age} years old.")

user_name = input("Enter your name: ")
user_age = input("Enter your age: ")

print_info(user_name, user_age)