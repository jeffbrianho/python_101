# Ask for a first number
# Ask for a second number
# Ask for the type of operation
# Print out the value of the operation from number 1 and 2'

import json

# Load the messages from the JSON file
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# Now 'MESSAGES' contains the loaded messages as a Python dictionary

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

while True:
    prompt('What is the language? Enter "en" for english or "rus" for Russian.')
    lang = input()

    prompt(MESSAGES[lang]['welcome'])

    prompt(MESSAGES[lang]['number_1'])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES[lang]["invalid_number"])
        number1 = input()

    prompt(MESSAGES[lang]['number_2'])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES[lang]["invalid_number"])
        number2 = input()

    prompt(MESSAGES[lang]['operation'])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(MESSAGES[lang]['op_choice'])
        operation = input()

    match operation:

        case '1':
            output = float(number1) + float(number2)
        case '2':
            output = float(number1) - float(number2)
        case '3':
            output = float(number1) * float(number2)
        case '4':
            output = float(number1) / float(number2)
    prompt(f'{MESSAGES[lang]['result']} {output}')

    prompt(MESSAGES[lang]['another'])
    response = input()
    if response and response[0].lower() != 'y':
        break