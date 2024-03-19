from random import randint


MAIN_GAME_QUESTION = 'Find the greatest common divisor of given numbers.'


def data():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    given_numbers = (f'{random_number_1} {random_number_2}')
    divisors_1 = set()
    for i in range(1, random_number_1 + 1):
        if random_number_1 % i == 0:
            divisors_1.add(i)
    divisors_2 = set()
    for i in range(1, random_number_2 + 1):
        if random_number_2 % i == 0:
            divisors_2.add(i)
    common_divisors = divisors_1 & divisors_2
    max_divisor = max(common_divisors)
    correct_answer = str(max_divisor)
    return given_numbers, correct_answer
