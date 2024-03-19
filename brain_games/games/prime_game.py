from random import randint


MAIN_GAME_QUESTION = ('Answer "yes" if given number is prime. \
Otherwise answer "no".')


def data():
    random_number = randint(1, 100)
    if random_number < 2:
        correct_answer = False or 'no'
    else:
        all_divisors = set()
        for i in range(1, random_number + 1):
            if random_number % i == 0:
                all_divisors.add(i)
        prime_divisors = {1, random_number}
        divisor_difference = all_divisors.difference(prime_divisors)
        correct_answer = divisor_difference == set() and 'yes' or 'no'
    return random_number, correct_answer
