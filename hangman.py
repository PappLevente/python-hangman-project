
























# def play(word, lives):
#     pass

# play('Codecool', 6)

def letter_input():
    print('\033[H\033[J', end='')
    import string
    abc = string.ascii_lowercase
    print('\n')
    while True:  # Ezt a parancsot valahol láttam így alkalmazni. Nem értem az elvét, de működik.
        letter = input('Please guess a letter:')  # Mindent stringnek vesz, állítólag a python3-ban ez van.
        letter = letter.lower()
        if letter in abc:
            print(letter + '\n')  # Print helyett majd return kell, mikor beépítjük!
        if letter == 'quit':
            print('\033[1m\nGood-bye!\033[0m\n')
            quit()
        if letter not in abc:
            print('\033[1m\nPlease consider that only a letter can be guessed!\033[0m\n')


letter_input()
