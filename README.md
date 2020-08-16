<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Arcade
*[Anton Neike]*

*[Data-ber-08-20, Berlin & 16/08/2020]*

## Content
- [Project Description](#project-description)
- [Rules](#rules)
- [Organization](#organization)
- [Sources](#links)

## Project Description
I decided to build a little arcade. In my arcade you can choose between two games for now:

<br>1 - Guess the number
<br>2 - Hangman

## Rules
Guess the number: 
<br>The rules for this game are quite simple. At the beginning of the game you can choose between three "levels". The levels just define in what range the computer will randomly choose a number. After having chosen the level you want to play at, start guessing. If the number you guessed is lower or higher than the randomly chosen number from the computer, the game will tell you to either guess higher or lower. Once you found the number the game is over and the computer will tell you how many tries it took you.

Hangman:
<br>At the beginning of the game you can choose between three "levels". The levels just define the difficulty of the word you will have to guess. After having chosen the level you want to play at, start guessing letter by letter. If the letter you guess is in the word to be guessed, the game will display you all the same letters in the word. If the letter is not contained in the word, a portion of the hangman is added and you will be asked to guess another letter. The game is won if all the letters of the word have been guessed before the hangman is completed. the game is lost if the Hangman is completed, meaning after 6 tries, before having guessed all the letters contained in the word. 


## Organization
In my repository you will find several files:

<br>1 - Main.py -> It launches the arcade and calls the diffrent game functions
<br>2 - Guess_the_number.py -> Contains the game function for the game Guess the number
<br>3 - Hangman.py -> Contains the game function for the game hangman
<br>4 - Hangman_extras.py -> Contains a list with the ASCII art for hangman and the dictionaries

## Sources
I used the following sources: 
https://randomword.com/
https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c