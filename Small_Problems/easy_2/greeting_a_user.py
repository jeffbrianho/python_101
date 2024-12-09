# Write a program that asks for user's name, then greets the user. If 
# the user appends a ! to their name, the computer will yell the 
# greeting (print it using all uppercase).

#pseduocode:
# start with asking for input of a name
# use a function to determine if the name has a "!"
# if true use a method to change name to .upper()
# if false return input
# use another function to determine output 
# if has ! output why are we yelling
# else print hello name

# def get_name():
#     name = input('What is your name? ')
#     return name

# def is_exclamation(calling):
#     if '!' in calling:
#         return calling.upper()
#     else:
#         return calling

# def greeting_type(name_type):
#     if '!' in name_type:
#         print(f'HELLO {is_exclamation(name_type)}! WHY ARE WE YELLING?')
#     else:
#         print(f'Hello {name_type}.')

# greeting_type(get_name())

# Too complex and harder to read!

name = input('What is your name? ')

if name.endswith('!'):
    print(f'HELLO {name.upper()}, WHY ARE WE YELLING?')
else:
    print(f'Hello, {name}.')
    
# What is your name? Sue
# Hello Sue.

# What is your name? Bob!
# HELLO BOB! WHY ARE WE YELLING?