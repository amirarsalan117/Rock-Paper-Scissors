import random 

list_play_options = ["rock", 'paper','scissors']



player_win = False


while not player_win:
    computer_hand = random.choice(list_play_options)
    player_hand = input('Rock-Paper-Scissors: ').lower()
    print('----------------')
    if player_hand == computer_hand:
        print('draw')
    elif player_hand == 'paper':
        if computer_hand == 'rock':
            print('you win',player_hand,'covers',computer_hand)
            player_win = True
        else:
            print('you lose', computer_hand, 'cut', player_hand)
    elif player_hand == 'scissors':
        if computer_hand == 'rock':
            print('you lose',computer_hand , 'smashes', player_hand)
        else:
            print('you win', player_hand , 'cut', computer_hand)
            player_win = True
    elif player_hand == 'rock':
        if computer_hand == 'paper':
            print('you lose', computer_hand , 'cut', player_hand)
        else:
            print('you win', player_hand , 'smashes', computer_hand)
            player_win = True
    else:
        print('this is not valid input, please enter agein')
    print('----------------')

    
    

