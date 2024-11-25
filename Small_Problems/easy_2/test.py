age = int(input("what is your current age? "))

print(f'You are {age} years old')
for year in range(10, 50, 10):
    print(f'in {year} years you will be {age + year} years old')