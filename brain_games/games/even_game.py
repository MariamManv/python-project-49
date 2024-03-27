from random import randint


MAIN_GAME_QUESTION = ('Answer "yes" if the number is even, \
otherwise answer "no".')


def is_even(number):
    return number % 2 == 0


MIN_NUMBER = 1
MAX_NUMBER = 1000


def create_data():
    random_number = randint(MIN_NUMBER, MAX_NUMBER)
    answer = is_even(random_number)
    if answer is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer
