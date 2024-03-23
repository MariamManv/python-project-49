from random import randint


MAIN_GAME_QUESTION = ('Answer "yes" if the number is even, \
otherwise answer "no".')


def is_even(number):
    return number % 2 == 0


def create_data():
    random_number = randint(1, 1000)
    answer = is_even(random_number)
    if answer is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer
