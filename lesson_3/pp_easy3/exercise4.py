my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)

# [{"first": 42}, {"second": "value2"}, 3, 4, 5] ; it 
# updates the dictionay as it makes a shallow copy for the dictionaries. 