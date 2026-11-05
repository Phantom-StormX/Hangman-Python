import Welcome
import Difficulty
from Display import *
hangman = [
    """
    =========
    """,
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    r"""
     -----
     |   |
     O   |
     |   |
      \  |
    =========
    """,
    r"""
     -----
      |  |
      O  |
      |  |
     / \ |
    =========
    """,
    r"""
    -----
      |  |
      O  |
    - | -|
     / \ |
    =========
    """
]

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
if pick_difficulty == '1':
    print(Difficulty.easy)
elif pick_difficulty == '2':
    print(Difficulty.medium)
elif pick_difficulty == '3':
    print(Difficulty.hard)
elif pick_difficulty == '4':
    print(Difficulty.super_hard)
elif pick_difficulty == '5':
    sys.exit()
else:
    print('not valid please try again')

print(guess_log(0,6))