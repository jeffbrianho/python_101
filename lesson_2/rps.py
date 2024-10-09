# Rock, Paper, Scissors

def prompt(welcome):
    print(f'===> {welcome}')

prompt('Welcome to Rock, Paper, Scissors!')

prompt('Enter the number 1 for Rock, 2 for Paper, or 3 for Scissor')
player_input = input()

while player_input != ('1', '2', '3'):
        print('Not a valid number')
        player_input = input()

print(player_input)