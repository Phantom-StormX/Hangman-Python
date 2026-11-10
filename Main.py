import Welcome
import Difficulty
import Display
import sys

# function for the choice of difficulty
def choose_difficulty():
    while True: # loops the difficulty selection until user chooses a valid choice
        pick_difficulty = input('''
Please pick a word difficulty by typing its number:
1. Easy
2. Medium
3. Hard
4. SUPER HARD!
5. Quit
''')
        new_word = ''
        if pick_difficulty == '1':
            return Difficulty.choose_random('1').lower() # lower() keeps all words lowercase
        elif pick_difficulty == '2':
            return Difficulty.choose_random('2').lower()
        elif pick_difficulty == '3':
            return Difficulty.choose_random('3').lower()
        elif pick_difficulty == '4':
            return Difficulty.choose_random('4').lower()
        elif pick_difficulty == '5':
            print('okay bye bye')
            sys.exit() # exits system
        else:
            print('Not valid; please try again.')

# function for guess logic and layout of the game (ex the _ _ _ part)
def guesses_and_layout(random_word):
    guessed = set()
    wrong_guess_list = []
    wrong_guess = 0
    max_attempt = 6
    start = True

    while wrong_guess < max_attempt:
        if wrong_guess == 0:
            print(Display.hangman_start)
        else:
            print(Display.hangman[wrong_guess -1])

        layout = ''
        for letter in random_word:
            if letter in guessed:
                layout += letter
            else:
                layout += ' _ '
        print(f'word: {layout}')

        if all(not letter.isalpha() or letter in guessed for letter in random_word): # if ALL the letters are true(as in actual letters), and is a part of the word, then you win
            print('You guessed the word!')
            return

        guess = input(f'''you have {wrong_guess} wrong guess(es) out of 6 attempts. 
guess a letter: ''').lower()

        if len(guess) == 2 or not guess.isalpha():
            print('please enter ONE ACTUAL letter')
            continue
        if guess in guessed:
            print('please pick another letter that you have NOT used')
            continue

        guessed.add(guess)
        if guess in random_word:
            print('yaya you got a letter!')
        else:
            wrong_guess_list.append(guess)
            wrong_guess += 1
            print("that letter isn't in the word.")
            #print(Display.hangman[wrong_guess - 1])
            print(f'letters that are not in the word: {wrong_guess_list}')


    print(f'You ran out of guesses. The word was: {random_word}')
    return False


def main_run():
    print(Welcome.Welcome_page)
    play_count = 1

    while True:
        random_word = choose_difficulty()
        guesses_and_layout(random_word)

        while True:
            play_again = input('Play again? (y/n): ').lower()


            if play_again in ('y'):
                print(f'cool you have played {play_count} time(s)! ')
                play_count += 1
                break

            elif play_again in ('n'):
                print(f'okie dokie thank you for playing {play_count} time(s)!')
                sys.exit()
            else:
                print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main_run()
