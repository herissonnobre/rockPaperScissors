import random
import re


def print_hi():
    while 1 < 2:
        print('\n')

        print('Rock, Paper, Scissors - Shoot!')

        user_choice = input('Choose your weapon [R]ock, [P]aper, or [S]cissors: ')

        if not re.match("[SsRrPp]", user_choice):
            print('Please choose a letter:')
            print('[R]ock, [S]cissors or [P]aper.')
            continue

        print('You chose: ' + user_choice)

        choices = ['R', 'P', 'S']

        opponent_choice = random.choice(choices)

        print('I chose: ' + opponent_choice)

        if opponent_choice == str.upper(user_choice):
            print('Tie! ')
            continue
        elif opponent_choice == 'R' and user_choice.upper() == 'S':
            print('Rock beats scissors, I win! ')
            continue
        elif opponent_choice == 'S' and user_choice.upper() =='P':
            print('Scissors beat paper, I win! ')
            continue
        elif opponent_choice == 'P' and user_choice.upper() == 'R':
            print('Paper beats rock, I win! ')
            continue
        else: 
            print('You win! ')
        

if __name__ == '__main__':
    print_hi()
