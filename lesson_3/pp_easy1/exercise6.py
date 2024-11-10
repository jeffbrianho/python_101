# Determine whether the name Dino appears in the strings below -- check each string separately:

str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

print(True if str1.find("Dino") != -1 else False)
print(True if str2.find("Dino") != -1 else False)

# easier!
'Dino' in str1  # False
'Dino' in str2  # True