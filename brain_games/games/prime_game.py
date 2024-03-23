from random import randint


MAIN_GAME_QUESTION = ('Answer "yes" if given number is prime. \
Otherwise answer "no".')


def is_prime(number):
    if number < 2:
        return False
    else:
        for i in range(2, (number // 2) + 1):
            if number % i == 0:
                return False
        return True


def create_data():
    random_number = randint(1, 100)
    answer = is_prime(random_number)
    if answer is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer
