# What does this nested function code with nonlocal variables print?
# <!---->
# # python

def counter():
    count = 0 
    def increment():
        nonlocal count # 0
        count += 1
        return count # 1
    return increment # count = 1

my_counter = counter() # my_counter will remember count 
print(my_counter()) # 1
print(my_counter()) # 2
print(my_counter()) # 3