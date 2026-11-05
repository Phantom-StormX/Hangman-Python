import Welcome
import Difficulty
import Display
import sys

print(Welcome.Welcome_page)

pick_difficulty = input('''
please pick a word difficulty by typing 
and entering its corresponding number:
1. Easy
2. Medium
3. Hard
4. SUPER HARD!
5. Quit
''')

random_word = ''
if pick_difficulty == '1':
    random_word = Difficulty.easy
elif pick_difficulty == '2':
    random_word = Difficulty.medium
elif pick_difficulty == '3':
    random_word = Difficulty.hard
elif pick_difficulty == '4':
    random_word = Difficulty.super_hard
elif pick_difficulty == '5':
    sys.exit()
else:
    print('not valid please try again')

guessed = []
wrong_guess_list = []
wrong_guess = 0
max_attempt = 6

while wrong_guess < max_attempt:
    layout = ''
    for letter in random_word:
        if letter in guessed:
            layout += letter + " "
        else:
            layout += '_' * len(letter)
            print(Display.hangman[wrong_guess])
            print(f'word:{layout} ')
        guess = input('guess a letter: ').lower()
        print(guess)

        if len(guess) != 1 or not guess.isalpha():
            print('please enter ONE ACTUAL letter')
        elif guess in guessed:
            print('please pick another letter that you have NOT used:')
            guessed.append(guess)

        if guess != letter:
            wrong_guess += 1
            wrong_guess_list.append(guess)
            print("hey that letter isn't in the word.")
            print(f'letters that are not in the word: {wrong_guess_list}')
        else:
            print('yay you guessed the right letter!')
