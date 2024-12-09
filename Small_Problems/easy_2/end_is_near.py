# Write a function that returns the next to last word in the string argument.

# Words are any sequence of non-blank characters.

# You may assume that the input string will always contain at least two words.



def penultimate(sentence):
    if len(sentence.split()) % 2 != 0:
        index = (len(sentence) // 2) - 1
        return (sentence.split()[index])
    else:
        return 'There is no middle word!'


# These examples should print True
# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")

print(penultimate('1 2 3'))
# edge case middle word

