#What does the last line in the following code output?

dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)


print(num_list)
print(dictionary)

# [1, 2]
# {'first': [1, 2]}
# it is a nested element and therefore is affected by the append mutation. it points to an object
