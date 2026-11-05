import Difficulty
import Main

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
# wrong_guess = 0
# max_attempt = 6

def guess_log(wrong_guess,max_attempt):
    guessed = []
    while wrong_guess < max_attempt:
        layout = ''
        for letter in Main.pick_difficulty:
            if letter in guessed:
                layout += letter
            else:
                layout += '_'
        return(hangman[wrong_guess])
        return f'word:{layout} '
        if '_' not in layout:
            return'yay! you got the word!'