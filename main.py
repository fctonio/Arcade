import Guess_the_number as gtn
import Hangman as hg


game = 0
arcade = 1

while arcade == 1: 
    if game == 0:
        game = int(input("Welcome to my Ironhack arcade! \n\nYou can choose from the following games:\n\n1 - Guess the number\n\n2 - Hangman\n\n3 - Exit arcade\n\n"))
    elif game == 1:
        game = gtn.guess_the_number()
    elif game == 2:
        game = hg.hangman()
    elif game == 3:
        arcade = 0
    else:
        game = int(input('Please input a number from 1 to 3: \n\n'))
print("Thank you for having played in our arcade!\n\n")
