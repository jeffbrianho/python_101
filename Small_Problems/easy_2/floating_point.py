# Write a program that prompts the user for two positive numbers 
# (floating-point), then prints the results of the following operations 
# on those two numbers: addition, subtraction, product, quotient, floor quotient, 
# remainder, and power. Do not worry about validating the input.

num1 = float(input('===> Enter the first number: \n'))
num2 = float(input('===> Enter the second number: \n'))

print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num1} - {num2} = {num1 - num2}')
print(f'{num1} * {num2} = {num1 * num2}')
print(f'{num1} / {num2}  = {num1 / num2}')
print(f'{num1} // {num2}  = {num1 // num2}')
print(f'{num1} % {num2}  = {num1 % num2}')
print(f'{num1} ** {num2}  = {num1**num2}')

# use a case/match
def calculate(first, second, operator):
    match operator:
        case '+':  return first + second
        case '-':  return first - second
        case '*':  return first * second
        case '/':  return first / second
        case '//': return first // second
        case '%':  return first % second
        case '**': return first ** second

first_float = float(input("==> Enter the first number:\n"))
second_float = float(input("==> Enter the second number:\n"))
for operator in ['+', '-', '*', '/', '//', '%', '**']:
    operation = f"{first_float} {operator} {second_float}"
    result = calculate(first_float, second_float, operator)
    print(f"==> {operation} = {result}")