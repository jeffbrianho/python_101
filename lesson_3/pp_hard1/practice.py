def add_element(my_list):
    print(id(my_list))
    my_list = my_list + [4]
    print(id(my_list))

my_list = [1, 2, 3]
print(id(my_list))
add_element(my_list)
print(my_list)