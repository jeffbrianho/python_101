# 2
# How can you determine whether a given string ends with an 
# exclamation mark (!)? Write some code that prints 
# True or False depending on whether the string ends with an exclamation mark.

def end_exclaim(word):
    if word[-1] == "!":
        print(True)
    else:
        print(False)

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

end_exclaim(str1)
end_exclaim(str2)

# alt

print(str1.endswith("!"))
print(str2.endswith("!"))