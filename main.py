import random 

list_play_options = ["rock", 'paper','scissors']

computer_hand = random.choice(list_play_options)

player_win = False


while not player_win:
    player_hand = input('Rock-Paper-Scissors').lower()
    if player_hand == computer_hand:
        print('Tie')
    

