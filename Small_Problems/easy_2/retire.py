# Build a program that displays when the user will retire and how 
# many years she has to work till retirement.

# What is your age? 30
# At what age would you like to retire? 70

# It's 2024. You will retire in 2064.
# You have only 40 years of work to go!

# X Obtain user age
# x Obtain retirement age
# print out the years left. 

from datetime import datetime

current_year = datetime.now().year

print('What is your age? ')
user_age = int(input())
print('At what age would you like to retire? ')
retire_age = int(input()) 

years_left = (retire_age - user_age)
print(f'\nIt\'s {current_year}. You will retire in {current_year + years_left}.\n'
      f'You have only {years_left} years of work to go!')




