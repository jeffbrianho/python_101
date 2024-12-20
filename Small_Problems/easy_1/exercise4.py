# Build a program that asks the user to enter the length and width of a room, in meters, 
# then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

# PEDAC Problem, example, data structure, algorithm, code

# PROBLEM:
# input: length integer
# input: width integer
# output: integer in meters and float in square feet 

#Domain: put in 2 inputs (x, y) as an integer
# calculate the area 2 times; x * y and x * 10.7639 and y * 10.7639 for feet
# output in a print for integer and float consider use of f string for labels

#mental model uses straight math for the problem using products ARITHMATIC
# use and input for 2 arguements and assign it 
# x * y and (x * 10.7639 * 10.7639 * y)

# DATA STRUCTURE: use input(x, y) and arithmatic
# ALGORITHM; use multiplication for both outputs and create a variable for each

# CODE
print('Enter the measurement type(m for meters, f, for feet)')
measurement = input()

if measurement == 'm':

    length = int(input("enter length in meters "))
    width = int(input('enter width in meters '))

    print((f'The area in meters is {(length * width):.2f} square meters,'
        f'and the area in feet is {(length * width * 10.7639):.2f} square feet'))
elif measurement == 'f':

    length = int(input("enter length in feet "))
    width = int(input('enter width in feet '))

    print((f'The area in feet is {(length * width):.2f} square feet,'
        f'and the area in meters is {(length * width / 10.7639):.2f} square meters'))
else:
    print('Must enter "m" or "f"!')
