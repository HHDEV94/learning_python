import random


def play_game():
    user_option = input(
        'Choice an option: "rk" to rock, "pr" to paper or "sc" to scissors. \n').lower()
    computer_option = random.choice(['rk', 'pr', 'sc'])

    if user_option == computer_option:
        return print(f'DRAW!!!, Both chose {user_option}')

    if player_win(user_option, computer_option):
        return print(f'Congratulations, You have won the Game!!! You chose {user_option} and Pc chose {computer_option}')

    return print(f'Sorry, You have lost :(. You chose {user_option} and Pc chose {computer_option}  Try again!!!')


def player_win(player, opponent):
    if ((player == 'rk' and opponent == 'sc') or (player == 'sc' and opponent == 'pr') or (player == 'pr' and opponent == 'rk')):
        return True
    else:
        return False

# Return True if player win the game
# Rock beats scissors (rk > sc)
# Scissors beats paper (sc > pr)
# Paper beats rock (pr > rk)


play_game()
