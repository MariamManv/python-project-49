from random import randint


RULES_OF_THE_GAME = ('Answer "yes" if given number is prime. \
Otherwise answer "no".')


def is_prime(number):
    if number < 2:
        return False
    else:
        for i in range(2, (number // 2) + 1):
            if number % i == 0:
                return False
        return True


MIN_NUMBER = 1
MAX_NUMBER = 100


def get_question_and_correct_answer():
    random_number = randint(MIN_NUMBER, MAX_NUMBER)
    if is_prime(random_number) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer
