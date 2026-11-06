import Welcome
import Difficulty
import Display
import sys


def choose_word():
    while True:
        pick_difficulty = input('''
Please pick a word difficulty by typing its number:
1. Easy
2. Medium
3. Hard
4. SUPER HARD!
5. Quit
''').strip()

        if pick_difficulty == '1':
            return Difficulty.easy.lower()
        elif pick_difficulty == '2':
            return Difficulty.medium.lower()
        elif pick_difficulty == '3':
            return Difficulty.hard.lower()
        elif pick_difficulty == '4':
            return Difficulty.super_hard.lower()
        elif pick_difficulty == '5':
            sys.exit()
        else:
            print('Not valid; please try again.')


def guesses_and_layout(random_word):
    guessed = set()
    wrong_guess_list = []
    wrong_guess = 0
    max_attempt = 6

    while wrong_guess < max_attempt:
        layout = ''
        for letter in random_word:
            if letter in guessed:
                layout += letter
            else:
                layout += '_'
        print(f'word: {layout}')

        if all(not letter.isalpha() or letter in guessed for letter in random_word):
            print('You guessed the word!')
            return

        print(Display.hangman_start)
        guess = input('guess a letter: ').strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print('please enter ONE ACTUAL letter')
            continue
        if guess in guessed:
            print('please pick another letter that you have NOT used')
            continue

        guessed.add(guess)
        if guess in random_word:
            print('yaya you got a letter!')
        else:
            wrong_guess += 1
            wrong_guess_list.append(guess)
            print("that letter isn't in the word.")
            print(Display.hangman[wrong_guess-1])
            print(f'letters that are not in the word: {wrong_guess_list}')

    print(f'You ran out of guesses. The word was: {random_word}')


def main_run():
    print(Welcome.Welcome_page)
    random_word = choose_word()
    guesses_and_layout(random_word)


if __name__ == "__main__":
    main_run()