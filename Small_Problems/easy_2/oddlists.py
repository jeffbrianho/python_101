# Write a function that returns a list that contains every other element 
# of a list that is passed in as an argument. The values in the returned 
# list should be those values that are in the 1st, 3rd, 5th, and so on elements 
# of the argument list.

# def oddities(lst):
#     new_lst = lst[::2]
#     return new_lst

def oddities(lst):
    new_lst = []
    for index in range(0, len(lst)):
        if index % 2 == 0:
            new_lst.append(lst[index])
            
    return new_lst

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True