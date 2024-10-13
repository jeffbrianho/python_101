# Rock, Paper, Scissors

import random

def prompt(welcome):
    print(f'===> {welcome}')

def choice(number):
    if int(number) == 1:
        return "Rock"
    if int(number) == 2:
        return "Paper"
    if int(number) == 3:
        return "Scissor"

while True:
    prompt('Welcome to Rock, Paper, Scissors!')

    prompt('Enter the number 1 for Rock, 2 for Paper, or 3 for Scissor')
    player_input = input()

    while player_input not in ['1', '2', '3']:
        print('Not a valid number, must choose "1", "2", or "3"')
        player_input = input()

    computer_pick = random.randrange(1, 4)

    print(f'You chose {choice(player_input)}')
    print(f'The computer chose {choice(computer_pick)}')

    match (int(player_input), computer_pick):
        case (1, 2):
            print("You Lose!")
        case (1, 3):
            print("You Win!")
        case (2, 1):
            print("You Win!")
        case (2, 3):
            print("You Lose!")
        case (3, 1):
            print("You Lose!")
        case (3, 2):
            print("You Win!")
        case _:
            print("You Tied!")
    prompt("Play Again? ('y' or 'n')")
    response = input()
    if response and response[0].lower() != 'y':
        break