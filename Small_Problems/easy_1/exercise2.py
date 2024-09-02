# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

# PEDAC (Problem, examples, data structure, algorithm, code)

# PROBLEM:
# Input: None
# Output integers

# Domain:
# print odd num from 1 to 99 inclusive on a separate line iterating on only odd numbers

# implicit requirements
# only whole numbers within a range new license integers only

# mental model:
# using a range to iterate over only odd numbers 1,100,2
# can also use while loops

# EXAMPLE:
# print(range(1, 100, 2))

# DATA STRUCTURE:
# use a range with integers

# ALGORITHM:
# while num < 100:
#     if num % 2 == 0 print num
# num += 1

# CODE:

# print(list(range(1, 100, 2)))

# does not create a new line

# nums = list(range(1, 100, 2))
# for num in nums:
#         print(num)

# # bonus:

# num = 1
# while num < 100:
#     if num % 2 == 1:
#         print(num)
#     else:
#         next
#     num += 1

 # LS answer
 # for number in range(1, 100):
 #      if number % 2 ==1:
 #          print(number)
 # 

# for number in range(1, 100, 2):
#     print(number)  
 # 
 # 
 # pretty much the same but makes the iteration direct
 # 
 #  
                