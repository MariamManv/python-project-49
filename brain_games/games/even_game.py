from random import randint


MAIN_GAME_QUESTION = ('Answer "yes" if the number is even, \
otherwise answer "no".')


def data():
    random_number = randint(1, 1000)
    correct_answer = random_number % 2 == 0 and 'yes' or 'no'
    return random_number, correct_answer
