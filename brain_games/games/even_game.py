from random import randint


MAIN_GAME_QUESTION = ('Answer "yes" if the number is even, \
otherwise answer "no".')


def is_even():
    random_number = randint(1, 1000)
    if random_number % 2 == 0:
        return random_number, True
    else:
        return random_number, False


def data():
    random_number, answer = is_even()
    if answer is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer
