
import random
import string
import os


def load_words(file_name):
        wordlist = list()
        #path = os.getcwd() + '/hangman-python-AttilaNA/'
        print(file_name)
        with open(file_name) as f:
            for line in f:
                wordlist.append(line.rstrip('\n'))
        return wordlist


def get_random_word():
    print('\033[H\033[J')
    print('\n')
    print('Let\'s play Hangman!')
    print('\n')
    return random.choice(wordlist)


def choose_level():
    level = ()
    while level != '1' or '2' or '3':
        level = input('Choose a level of difficulty among 1/2/3:')
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
            print('\nPlease consider that only a letter can be guessed!\n')


def occurance(brought_word, given_guess_letter):
    start = 0
    end = len(brought_word) - 1
    list = []
    while start <= end:
        if given_guess_letter == brought_word[start].lower():
            list.append(start)
        start += 1
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
    return display_list


def show_hit(displayed_list, word_in_list, hit_list):
    for item in hit_list:
        displayed_list[item] = word_in_list[item]
    return displayed_list


def no_lives(remaining_lives, word):
    if remaining_lives == 0:
        print('\033[H\033[J')
        print('\033[1m')
        print('Game Over')
        print('\033[0m')
        print(''.join(word))
        print('\n')
        return True
    else:
        return False


def no_underscore(underscore):
    if underscore.count('_ ') == 0:
        print('\033[1m')
        print('You are awesome! You\'ve won!')
        print('\033[0m')
        return True
    else:
        return False


def fill_list(tip, previous_letters):
    if tip not in previous_letters:
        previous_letters.append(tip)
        return previous_letters
    else:
        return previous_letters


def dicrease_lives(life, word, tip, letter_list):
    if tip in letter_list:
        return life
    elif tip in word:
        return life
    else:
        life = life - 1
        return life


def play(word, lives):  # Ne felejstsük el átadni egyik függvény paraméterét a másiknak
    word_in_list = convert_str_to_list(word)
    # print(word_in_list)
    displayed_word_in_list = get_display_list(word_in_list)
    print(''.join(displayed_word_in_list))
    is_it_win = False
    is_it_lose = False
    used_letters = []
    while is_it_win == False and is_it_lose == False:
        guess_letter = get_guess()
        print('\033[H\033[J')
        occurance_indexes = occurance(word, guess_letter)
        displayed_word_in_list = show_hit(displayed_word_in_list, word_in_list, occurance_indexes)
        print(''.join(displayed_word_in_list))
        lives = dicrease_lives(lives, word_in_list, guess_letter, used_letters)
        print('You have ' + str(lives) + ' live(s) left')
        used_letters = fill_list(guess_letter, used_letters)
        print('Previous guesses:' + (','.join(used_letters)))
        is_it_win = no_underscore(displayed_word_in_list)
        is_it_lose = no_lives(lives, word_in_list)


wordlist = load_words('countries.txt')
first = get_random_word()
second = choose_level()

play(first, second)
