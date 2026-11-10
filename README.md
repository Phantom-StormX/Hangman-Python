<h1 align="center">Welcome to Hangman! </h1>
<p align="center">Coded in Python by: Izzy Pichler :)

## Overview

- A classic game of hangman that was made out of python
- consists of 4 different difficultys, each difficulty has at least 10 words
  - Organized by actual difficulty in guessing the word, not by length
  - Super hard difficulty is both in length and actual difficulty in guessing 
- Keeps track of how many times you've played the game, and how many wrong guesses you have
  - you only have 6 attempts for each difficulty 
  
## How to Run

1. Open the project by cloning the repo in Pycharm.
2. Make sure the version of python is 3.14.5
3. Run the launcher 'Main.py' from the IDE.

If you are running from a compiled output folder, make sure the application is launched from the correct main entry point.    

## Logic:

  - This game operates based off of loops, variables, conditionals and functions. The main steps can be broken down into the following broad steps:
    - Choose Difficulty: Asks the user what difficulty they want, and depending on what they choose will make the words harder
    - Attempts in guessing: If the letter is valid in the word that was randomized
    - Actual hangman layout: Tracks the amount of letters in randomized word and prints out '_'
    - Play again: Asks user if they want to play again
    
## Choose Difficulty:

  - The code begins by welcoming the player, telling them what game it is, then asks the user what word difficulty they want
  - the user then chooses the corresponding number with the difficulty
    - when they choose the difficulty, the computer goes to the list the corresponds with the difficulty and randomizes and choses one of the values in the list
    
## Layout and guesses:

  - Grabs the randomized word, takes it's length and prints out '_' for each letter
  - When the user guesses a letter, it goes through the word to see if the letter is actually in the word
    - if the letter is in the word it will change the '_' to the corresponding letter
  - Checks if user's guess is a valid letter
    - valid as in a real letter (using alpha()) and if the length of the input is only one
  - if the letter is wrong it adds one to wrong guesses, and if they guessw wrongly 6 times, they will lose and the game will be over     
    
## Main:

  - Runs literally almost everything in the project
    - it's a function that is ran by a boilerplate code(i think thats what it is called?)
  - has play again logic
    - if user wants to play again they will type 'y', and the computer will ask for a difficulty and then randomizes a brand new word
    - if user does not want to play again they will type 'n' and the project will exit   

## Challenges and Bugs:

  - I had a problem with making the computer read the letters in the word and print out '_'
  - During the play again logic it would not randomize the word again, so it would just repeat the last word used
  - The art would not print out when needed to print out
  - Functions would not go across files
    - I did want to put more research in it but it was not needed 
      
### Credentials
  - [https://www.geeksforgeeks.org/python/hangman-game-python/](url) help with the letter reading 
