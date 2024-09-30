# Ask for a first number
# Ask for a second number
# Ask for the type of operation
# Print out the value of the operation from number 1 and 2
def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False

prompt('Welcome to Calculator!')

prompt('What is the first number?')
number1 = input()

while invalid_number(number1):
    prompt("Hmm... that doesn't look like a valid number.")
    number1 = input()

prompt('What is the second number?')
number2 = input()

while invalid_number(number2):
    prompt("Hmm... that doesn't look like a valid number.")
    number2 = input()

prompt('What is the operation you would like to perform?'
      '\n 1) Add 2) Subtract 3) Multiply 4) Divide')
operation = input()

while operation not in ["1", "2", "3", "4"]:
    prompt('You must choose 1, 2, 3, or 4')
    operation = input()

match operation:

    case '1':
        output = int(number1) + int(number2)
    case '2':
        output = int(number1) - int(number2)
    case '3':
        output = int(number1) * int(number2)
    case '4':
        output = int(number1) / int(number2)
prompt(f'The result is: {output}')