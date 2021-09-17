import random
import string

def load_words(WORDLIST_FILENAME):
       wordlist = list()
       with open(WORDLIST_FILENAME) as f:
            for line in f:
                wordlist.append(line.rstrip('\n'))
       return wordlist




def get_random_word():
    print('\033[H\033[J')
    print('\n')
    print('\033[1m')
    print('Let\'s play Hangman!')
    print('\033[0m')
    print('\n')
    return random.choice (wordlist)


def choose_level():
    level = ()
    while level != '1' or '2' or '3':
        level = input('\033[1m\nChoose a level of difficulty among 1/2/3 = \033[0m')
        if level == '1':
            return 6
        elif level == '2':
            return 5
        elif level == '3':
            return 4
        else:
            print('\nPlease choose the level on that you\'d like to play the game!\n')


def get_guess():
    letter = ''
    abc = string.ascii_lowercase
    while letter != 'quit' or letter not in abc:
        letter = input('Please guess a letter:')
        letter = letter.lower()
        if letter in abc:
            return letter
        elif letter == 'quit':
            print('\033[1m\nGood-bye!\033[0m\n')
            quit()
        else:
            print('\033[1m\nPlease consider that only a letter can be guessed!\033[0m\n')


def occurance(brought_word, given_guess_letter):
    start = 0
    end = len(brought_word) - 1
    list = []
    while start <= end:
        if given_guess_letter == brought_word[start].lower():
            list.append(start)
        start += 1
    print(list)
    return list


def convert_str_to_list(str):
    word_list = []
    for char in str:
        word_list.append(char)
    return word_list


def get_display_list(list):
    display_list = []
    for item in list:
        if item == ' ':
            display_list.append(' ')
        else:
            display_list.append('_ ')
    print('\033[H\033[J')
    print('\n')
    print('Here comes the word you have to find out:\n')
    print(display_list)
    print('\n')
    return display_list


def show_hit(displayed_list, word_in_list, hit_list):
    for item in hit_list:
        displayed_list[item] = word_in_list[item]
    return displayed_list


def show_miss(decrease_lives, hit_list):
    if hit_list == []:
        decrease_lives = decrease_lives - 1
        print('You have ' + str(decrease_lives) + ' remaining guesses.')
    return decrease_lives


# Imi
def no_lives(remaining_lives):
    if remaining_lives == 0:
        print('\033[H\033[J')
        print('\033[1m')
        print('Game Over')
        print('\033[0m')
        print('\n')
        return True
    else:
        return False


# Imi
def no_underscore(underscore):
    if underscore.count('_ ') == 0:
        print('\033[H\033[J')
        print('\033[1m')
        print('You are awesome! You\'ve won!')
        print('\033[0m')
        print('\n')
        return True
    else:
        return False


# Imi
def wrong_list_add(wrong_list, guess_letter):
        wrong_list.append(guess_letter)


def play(word, lives):  # Ne felejstsük el átadni egyik függvény paraméterét a másiknak
    word_in_list = convert_str_to_list(word)
    displayed_word_in_list = get_display_list(word_in_list)
    print('You have ' + str(lives) + ' remaining guesses.')  # Imi
    print('\n')
    is_it_win = False
    is_it_lose = False
    wrong_list = []
    while is_it_win == False and is_it_lose == False:  # Imi
        guess_letter = get_guess()
        occurance_indexes = occurance(word, guess_letter)
        displayed_word_in_list = show_hit(displayed_word_in_list, word_in_list, occurance_indexes)
        print(displayed_word_in_list)
        if guess_letter not in wrong_list:  # Imi
            lives = show_miss(lives, occurance_indexes)  # Imi
        if guess_letter in wrong_list:  # Imi
            print('Already tipped.')  # Imi
        if occurance_indexes == [] and guess_letter not in wrong_list:  # Imi
            wrong_list_add(wrong_list, guess_letter)  # Imi
        #  print('You have ' + str(lose_life) + ' remaining guesses.')
        #  print('You have ' + str(lives) + ' remaining guesses.')  # Imi
        is_it_win = no_underscore(displayed_word_in_list)
        is_it_lose = no_lives(lives)  # Imi


wordlist = load_words('countries.txt')
first = get_random_word()
second = choose_level()

play(first, second)
