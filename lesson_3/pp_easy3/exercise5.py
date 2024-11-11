# The following function unnecessarily uses two return statements to return boolean values. 
# Can you rewrite this function so it only has one return statement 
# and does not explicitly use either True or False?

# def is_color_valid(color):
#     if color == "blue" or color == "green":
#         return True
#     else:
#         return False
    
# def is_color_valid(color):
#     return color == "blue" or color == "green"

def is_color_valid(color):
    return color is "blue" or color is "green"

# launch school 
# def is_color_valid(color):
   # return color in ["blue", "green"]

co1 = "blue"
co2 = "green"
co3 = "red"

print(is_color_valid(co1))
print(is_color_valid(co2))
print(is_color_valid(co3))