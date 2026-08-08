import random

words = ["apple", "banana", "grapes", "papaya", "orange", "pear"]
word = random.choice(words)

guessed = []
wrong_guesses = 0
max_attempts = 6

hangman = [    """
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
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """]

while wrong_guesses < max_attempts:
    display = ""
    for letter in word:
        if letter in guessed:
            display = letter + ""
        else:
            display = "_ "

    print(hangman[wrong_guesses])

    if guessed is words:
        print("Congratulations!! You Won")
        break
    guess = input("Enter Your Word: ").islower()

    