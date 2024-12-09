# a function that determines the index of the 3rd occurrence of a given 
# character in a string. For instance, if the given character is 'x' and 
# the string is 'axbxcdxex', the function should return 6 
# (the index of the 3rd 'x'). If the given character does not occur at least 
# 3 times, return None.

my_str = 'axbxcdxex'
how_many_times = 2
def third_time_index(letters, object):
    counter = 0
    index = 0
    while (index < len(letters)) and (counter != how_many_times):
        if letters[index] == object:
            counter += 1
            index += 1
        else:
            index += 1
    if counter == how_many_times:
        return (f'The character \'{object}\' is found at index {index - 1} on the {how_many_times} time!')
    else:
        return None

print(third_time_index(my_str, 'x'))