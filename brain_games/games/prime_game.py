from random import randint


MAIN_GAME_QUESTION = ('Answer "yes" if given number is prime. \
Otherwise answer "no".')


def prime():
    random_number = randint(1, 100)
    if random_number < 2:
        return random_number, False
    else:
        for i in range(2, (random_number // 2) + 1):
            if random_number % i == 0:
                return random_number, False
        return random_number, True


def data():
    random_number, answer = prime()
    if answer is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer
