from random import randint


MAIN_GAME_QUESTION = ('Answer "yes" if given number is prime. \
Otherwise answer "no".')


def prime():
    random_number = randint(1, 100)
    if random_number < 2:
        return random_number, False
    else:
        all_divisors = set()
        for i in range(1, random_number + 1):
            if random_number % i == 0:
                all_divisors.add(i)
        prime_divisors = {1, random_number}
        divisor_difference = all_divisors.difference(prime_divisors)
        if divisor_difference == set():
            return random_number, True
        else:
            return random_number, False


def data():
    random_number, answer = prime()
    if answer is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer
