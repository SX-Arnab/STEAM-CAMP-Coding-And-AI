# # Work 1 :  Generate 6 random numbers between 1 and 50 for a lottery simulation.
# from random import randint
# for i in range(1,7):
#     print(randint(1,50))

# # Work 2 :  Create a random password using letters and digits for account security.
# from random import choice

# key = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
#     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
#     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
#     '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
# ]

# len = int(input("Enter the len of password : "))

# for i in range(len+1):
#     passwd = choice(key)
#     print(passwd, end = "" )
# print('\n')


# # Work 3 :  Randomly select a question from a list of practice questions to quiz yourself.
# # Using Choice func again

# questions = [
#     ["What is your name?"],
#     ["How old are you?"],
#     ["Where do you live?"],
#     ["What is your favorite color?"],
#     ["What do you you do for work?"],
#     ["What are your hobbies?"],
#     ["What is your favorite food?"],
#     ["What languages do you speak?"],
#     ["What is your biggest goal?"],
#     ["What makes you happy?"]
# ]

# for question in questions:
#     random_question = choice(question)

# print(random_question)


# Work 4 : 
'''
 Randomly choose a recipe from a CSV file
 of dishes to decide what to cook today.
'''
import csv
from random import choice

with open('dishes.csv', 'r') as f:
    content = csv.DictReader(f)
    list_content = list(content)

# print(content)

random_dish = choice(list_content)
print(random_dish)