# Write a function that takes one integer argument and returns 
# True when the number's absolute value is odd, False otherwise.

# PEDAC - problem, examples, data, algorithm, code
# 
# PROBLEM

# Problem input/output
#   input: a single integer
#   output: Boolean

# Problem domain
#     is it an odd number? if yes print True

# implicit requirements:
# whole numbers that are only positive
# how will they be entered? as a call function arguement
# what to do if nothing is entered? default to False?

# explicit requirements:
# must use absolute value of a number

# Mental Model (the how)
# call a function and provide an arguement
# if the arguement % 2 is 0 print false

# EXAMPLES

# Test cases:
# input (1)
# output True

# input (2)
# output False

# input -2
# output False

# input -1
# output True

# input 0
# output False

# input[]
# output False or error?

# DATA STRUCTURE
# integers modulo and make absolute value 
# into a Boolean with if statement
    
# ALGORITHM
# create a function with a single parameter

# determine if parameter is negative and make absolute value 
# with if statement < 0
# if less than 0, multiply by -1
    
# take the value and modulo 2

# if result is 1, print True

# else print False

# CODE with intent

# def odd_number(num):
#     if num < 0:
#         value = num * -1
#     else:
#         value = num

#     print(value)    
        
#     if value % 2 == 1:
#         return True
#     else:
#         return False
        
# print(odd_number())

# using hint of abs:

# def odd_number(num):
#     if abs(num) % 2 == 1:
#         return True
#     else:
#         return False



#LS answer: dont forget about returning true automatically if the equation is truthy

def is_odd(number):
    return abs(number) % 2 == 1

print(is_odd(-0))