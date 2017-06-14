import random

options = {
    'Rock': ['Lizard', 'Scissors'],
    'Paper': ['Rock', 'Spock'],
    'Scissors': ['Paper', 'Lizard'],
    'Lizard': ['Spock', 'Paper'],
    'Spock': ['Scissors', 'Rock']
}

player_wins = 0
computer_wins = 0

while True:
    print('Score: Player - Computer {}:{}'.format(player_wins, computer_wins))
    player_choice = input('Rock, Paper, Scissors, Lizard, Spock? (Ctrl+C to stop): ')
    if player_choice not in options.keys():
        continue
    computer_choice = random.choice(list(options.keys()))
    print('Computer choice: {}'.format(computer_choice))
    if computer_choice in options[player_choice]:
        print('Player wins!')
        player_wins += 1
    elif player_choice in options[computer_choice]:
        print('Computer wins!')
        computer_wins += 1
    else:
        print('Draw!')