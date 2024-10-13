# rock paper scissors with help

import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

def prompt(message):
    print(f'===> {message}')

def player_wins(players_choice, computers_choice):
    if ((players_choice == 'rock' and computers_choice == 'lizard') or
        (players_choice == 'rock' and computers_choice == 'scissors') or
        (players_choice == 'paper' and computers_choice == 'spock') or
        (players_choice== 'paper' and computers_choice == 'rock') or
        (players_choice == 'scissors' and computers_choice == 'lizard') or
        (players_choice == 'scissors' and computers_choice == 'paper') or
        (players_choice == 'lizard' and computers_choice == 'paper') or
        (players_choice == 'lizard' and computers_choice == 'spock') or
        (players_choice == 'spock' and computers_choice== 'rock' ) or
        (players_choice== 'spock' and computers_choice == 'scissors')
        ):
        return True
    else:
        return False

def display_winner(player, computer):
    if player_wins(player, computer):
        prompt('You Win!')
    elif player == computer:
        prompt('It is a Tie!')
    else:
        prompt("Computer Wins!")

while True:

    PLAYER_WIN_COUNTER = 0
    COMPUTER_WIN_COUNTER = 0

    prompt(f"Welcome to {', '.join(VALID_CHOICES)}! Best of 5 Wins!")

    while (PLAYER_WIN_COUNTER < 3) and (COMPUTER_WIN_COUNTER < 3):
        prompt(f"Choose one: {', '.join(VALID_CHOICES)}")
        choice = input()

        while choice not in VALID_CHOICES:
            prompt('That is not a valid choice')
            choice = input()

        computer_choice = random.choice(VALID_CHOICES)

        prompt(f'You chose {choice}, computer chose {computer_choice}')
        display_winner(choice, computer_choice)

        if choice == computer_choice:
            continue
        if player_wins(choice, computer_choice):
            PLAYER_WIN_COUNTER += 1
        else:
            COMPUTER_WIN_COUNTER += 1

        prompt(f'Player wins = {PLAYER_WIN_COUNTER},'
        f'Computer wins = {COMPUTER_WIN_COUNTER}')

    prompt('Do you want to play again? (y/n)?')
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt('Please enter "y" or "n".')
        answer = input().lower()

    if answer[0] == 'n':
        break