import random as rd

def compare(your_number, pc_number, dict_dif):
    if your_number > pc_number:
        your_number = int(input('Guess lower: '))
    elif your_number < pc_number:
        your_number = int(input('Guess higher: '))
    else:
        your_number = int(input(f'Please input a number between 1-{dict_dif}'))
    return your_number

def guess_the_number():

    dict_dif = {1: 10, 2: 100, 3: 1000}

    difficulty = int(input('\nHi welcome to ou arcade game GUESSE THE NUMBER!\n\nFirst choose the difficulty of the game:\n\n1 - Easy (Guess a number between 0-10)\n\n2 - Medium (Guess a number between 0-100)\n\n2 - Hard (Guess a number between 0-1000)\n\nPlease choose by inputing 1, 2 or 3: '))
    your_number = int(input(f'\nPlease choose a number between 0-{dict_dif[difficulty]}: '))

    pc_number = rd.randrange(1,dict_dif[difficulty])
    counter = 0

    while your_number != pc_number:
        your_number = compare(your_number, pc_number, dict_dif[difficulty])
        counter = counter + 1

    game = int(input(f'You won!! It took you: {counter} tries\n\nPress 1 if you want to play again or 0 to Exit: '))
    return game