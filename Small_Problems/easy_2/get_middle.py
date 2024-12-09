# Write a function that takes a non-empty string argument and returns the 
# middle character(s) of the string. If the string has an odd length, you 
# should return exactly one character. If the string has an even length, 
# you should return exactly two characters.

# create function
# determine length of string using len(string)
# determine if len is even or odd
# if odd print len(string)// 2 as index - 1
# create variable for half of len
# if even print string[ and len -1 len//2]
# return characters

def middle_index(string):
    middle_index = len(string) // 2
    return middle_index

def center_of(string):
    if len(string) % 2 != 0:
        return string[middle_index(string)]
    else:
        return string[middle_index(string) - 1:middle_index(string) + 1]

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True