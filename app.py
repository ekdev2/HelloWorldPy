from utils import find_max
from ecommerce.shipping import calc_shipping
import random
import openpyxl as xl



# print('Eugene Krivenko')
# print('o----')
# print(' ||||')

# expression will write * 10 times
# print('*' * 10)

# variables
# price = 10
# rating = 4.9
# name = 'Eugene'
# is_published = True
# print(price)

# inputs
# name = input('What is your name? ')
# color = input('What is your favorite color? ')
# print(name + ' likes ' + color)

# converting string to int
# birth_year = int(input('Birth Year: '))
# age = 2021 - birth_year
# print(age)
# print(type(age))

# lbs to kg input conversion
# pounds = float(input('What is your weight (in lbs): '))
# print('your weight in kilograms is: ' + str((pounds * 0.45)))

# string
# print("Eugene's test")
# print('Eugene is the "man"')
# course = '''
# This is a multiline string!
#
# This is the big test
# '''
# print(course)

# string indexes
# course = 'Python for Beginners'
# print(course[0])
# print(course[-1])
# print(course[-2])
# print(course[0:3])
# print(course[0:])
# print(course[1:])
# print(course[:5])
# another = course[:]
# print(another)
# print (course[1:-1])

# formatted strings
# first = 'John'
# last = 'Smith'
# message = first + ' [' + last + '] is a coder'
# print(message)
# msg = f'{first} [{last}] is a coder'
# print(msg)
# course2 = 'Python for Beginners'
# print(len(course2))
# print(course2.upper())
# # case sensitive
# print(course2.find('P'))
# print(course2.find('Beginners'))
# print(course2.replace('Beginners', 'Absolute Beginners'))
# print('Python' in course2)

# arithmetic operations
# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)
# x = 10
# x = x + 3
# print(x)
# x -= 3
# print(x)
# order of operation/operator precedence

# Math functions
# round
# print(abs(-2.9))

# if statements
# is_hot = False
# is_cold = True
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print('Wear warm clothes')
# else:
#     print("it's a lovely day")
# print('Enjoy your day')

# if statement exercise
# house_price = 1000000;
# has_good_credit = True;
# if has_good_credit:
#     down_payment = house_price * .10
# else:
#     down_payment = house_price * .20
# print(f"Down payment: ${down_payment}")

# logical operators
# has_high_income = False
# has_good_credit = True
# if has_high_income and has_good_credit:
#     print('eligible for a loan');
# if has_high_income or has_good_credit:
#     print('eligible for a loan');
# not operator

# comparison operators
# name = 'testing'
# if len(name) < 3:
#     print('name must be at least characters')
# elif len(name) > 50:
#     print("name can be a maximum of 50 characters")
# else:
#     print("name looks good")

# exercise
# weight = input('Weight: ')
# lbs_or_kg = input('(L)bs or (K)g: ')
# if lbs_or_kg.upper() == "L":
#     result = float(weight) * 0.453592
#     unit_type = 'killograms'
# elif lbs_or_kg.upper() == "K":
#     result = float(weight) / 2.20462
#     unit_type = 'pounds'
# print(f"You are {result} {unit_type}")

# while loops
# i = 1
# while i <= 5:
#     print('*' * i)
#     i += 1

# while loop guessing game
# correct_number = 7
# guess_count = 0
# total_guesses = 3
# while guess_count < total_guesses:
#     guess = int(input('Guess: '))
#     if guess == correct_number:
#         print('you guessed right. Congrats!')
#         break
#     elif guess_count < total_guesses - 1:
#         print('incorrect, please try again')
#     guess_count += 1
# else:
#     print('incorrect. Your 3 chances are up. You lost!')


# while loop car game
quit_command = ''
previous_command = ''
# while True:
#     current_command = input('> ').upper()
#     if current_command == 'HELP':
#         print('''
# start - to start the car
# stop - to stop the car
# quit - to exit
#         ''')
#     elif current_command == 'START':
#         if previous_command == current_command:
#             print('Car already started')
#         else:
#             print('Car started...Ready to go!')
#     elif current_command == 'STOP':
#         if previous_command == current_command:
#             print('Car already stopped')
#         else:
#             print('Car stopped.')
#     elif current_command == 'QUIT':
#         quit_command = 'quit'
#         break
#     else:
#         print('Invalid Command')
#     previous_command = current_command

#for loops and range function
# for item in range(10):
#     print(item)

# for loop calculate price
# prices = [10, 20, 30]
# total = 0
# for item in prices:
#     total += item
# print(total)

# nested loop exercise
# numbers = [5, 2, 5, 2, 2]
# for total_x in numbers:
#     current_line = ''
#     for x in range(total_x):
#         current_line += 'x'
#     print(current_line)


# list exercise
# numbers = [1, 6, 2, 4, 5]
# largest_number = numbers[0]
# for item in numbers:
#     if item > largest_number:
#         largest_number = item
# print(largest_number)

# 2 dimensional lists

# list functions

# list exercise - remove dup number
# numbers = [1, 2, 5, 2, 2]
# unique_numbers = []
# for item in numbers:
#     if item not in unique_numbers:
#         unique_numbers.append(item)
#
# print(unique_numbers)

# tuples - immutable lists

# unpacking - can be used for lists, tuples

# dictionary - like json objects

# phone number exercise
# number_words = {
#     "0": "Zero",
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine"
# }
# phone = input('Phone: ')
# output = ''
# for item in phone:
#     output += number_words.get(item, "!") + ' '
# print(output)

# functions
# def convert_words_to_emojis(message):
#     words = message.split(" ")
#     emojis = {
#         ":)": "😊",
#         ":(": "☹"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
#
#
# input_message = input("> ")
# print(convert_words_to_emojis(input_message))

# exceptions
# try:
#     age = int(input('Age: '))
#     print(age)
# except ValueError:
#     print('invalid value')

# comments

# classes
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f'I am {self.name}')
#
#
# p = Person('Eugene')
# p.talk()
#
# p = Person('Robert')
# p.talk()

# inheritance

# modules - function below is imported
# numbers = [1, 8, 2, 4, 5]
# print(find_max(numbers))

# packages - container for multiple related modules
# calc_shipping()

# Python Module Index - list of all the built in modules

# example - using random function from buult in library

# random exercise
# class Dice:
#     def roll(self):
#         random_numbers = (random.randint(1, 6), random.randint(1, 6))
#         return random_numbers
#
#
# dice = Dice()
# print(dice.roll())

# files and directories

# pypi

# exercise excel automation

# machine learning exercise
# import the data
# clean the data
# split data into training/test sets
# create a model - selecting an algorithm to analyze the data
# train the model
# make predictions
# evaluate and improve



























