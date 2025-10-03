##################################################################################
#  Program Name   : ex8.py
#  Author         : Arjan Singh Chahal
#  Task           : program keeps asking the user for words until they type exit
##################################################################################

while True:
    word = input("Enter a word (type 'exit' to quit): ")
    if word.lower() == 'exit':
        break