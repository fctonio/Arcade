import random
from Hangman_extras import hangstatus, dict_hard, dict_medium, dict_easy

#Defining funtions

#Function which is called so that the player can choose from what dict the word is picked
def difficulty():
    level = int(input("\nHi, welcome to hangman! Before we start, choose at what difficulty level you want to play this game:\n\n1 - Easy (A country)\n\n2 - Medium (An object)\n\n3 - Hard (Words you probably didn\'t know even existed)\n\n"))
    if level == 1:
        return dict_easy
    elif level == 2:
        return dict_medium
    elif level == 3:
        return dict_hard
    else: 
        level = input('\nPlease choose between 1, 2 and 3: ')

#Function for the letter input from the player
def player_input():
    return input('\nGuess a letter which might be in the word: ').lower()

def verify_input(player_letter):
    if len(player_letter) == 1 and player_letter.isalpha():
        return True
    else:
        return False

#Function that updates the word the player is guessing
def player_word_update(computer_word_list, player_letter, player_word):
    indices = [i for i, x in enumerate(computer_word_list) if x == player_letter]
    for i in indices:
        player_word[i] = player_letter
    return player_word   

#Game function called in main
def hangman ():

    #Defining variables
    counter = 0
    level = difficulty()
    computer_word = random.choice(list(level.keys()))
    computer_word_list = list(computer_word)
    player_word = ["_"] * len(computer_word_list)
    fail_list = []

    while computer_word_list != player_word and counter <= 5:
        player_letter = player_input()
        if verify_input(player_letter):
            if player_letter in computer_word_list:
                player_word = player_word_update(computer_word_list, player_letter, player_word)
                print(f'\n{player_letter} is in the word!\n\n{player_word}')
            else:
                if player_letter not in fail_list:
                    fail_list.append(player_letter)
                    counter = counter + 1
                    print(f'\nTry again!\n\n{hangstatus[counter]} \n\n Letters not in the word: {fail_list}\n\n')
                else:
                    print(f'\nYou already tried {player_letter} and it was not in the the word')
        else:
            print('\nPlease only use letters and type them one at a time.')
    
    if counter >= 6:
        game = int(input(f'\nYou lost :(\n\nThe word was {computer_word}! {level.get(computer_word)}\n\nPress 2 if you want to play again or 0 to Exit: '))
    else:    
        game = int(input(f'\nYou won!!\n\nThe word was {computer_word}! {level.get(computer_word)}\n\nIt took you: {counter} tries\n\nPress 2 if you want to play again or 0 to Exit: '))
    return game