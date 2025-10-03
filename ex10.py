###############################################################################
#  Program Name   : ex10.py
#  Author         : Arjan Singh Chahal
#  Task           : Asks the user to enter the names of three friends and
#                   stores them in a list. Then, print out the names of the 
#                   friends.
###############################################################################


friends = []
for i in range(3):
    name = input(f"Enter the name of friend {i+1}: ")
    friends.append(name)

print("Your friends are:")
for friend in friends:
    print(friend)