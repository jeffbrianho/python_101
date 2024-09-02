# Print all even numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the even numbers?

# same process as before but with even numbers

#PEDAC
# PROBLEM:

# input: None
# output: integer

# Domain:
# print 2-98 inclusive while iterating only on the even numbers

# mental model:
# using a range to iterate over only even numbers 0,100,2
# can also use while loops

# EXAMPLE:
# print(range(1, 100, 2))

# DATA STRUCTURE:
# use a range with integers

# ALGORITHM:
# while num < 100:
#     if num % 2 == 0 print num
# num += 1

for num in range(2, 100, 2):
    print(num)