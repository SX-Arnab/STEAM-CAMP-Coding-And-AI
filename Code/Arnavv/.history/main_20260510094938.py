# Importing Modules
from random import randint, choice
from bs4 import BeautifulSoup


user = int(input("Enter a num: "))
num = randint(1, 101)

while user != num:
    if user>num:
        print('Lower')
        user
        break
    elif num>user:
        print("Higher")
        user
    elif user == num:
        print('You guessed Correctly')
        break