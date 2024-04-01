from random import randint


RULES_OF_THE_GAME = ('Answer "yes" if the number is even, \
otherwise answer "no".')


def is_even(number):
    return number % 2 == 0


MIN_NUMBER = 1
MAX_NUMBER = 1000


def get_question_and_correct_answer():
    random_number = randint(MIN_NUMBER, MAX_NUMBER)
    if is_even(random_number) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer
