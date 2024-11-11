a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))
print(id(a), id(b), id(c))

# all about the interning