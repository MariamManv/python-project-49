from random import randint
from brain_games.games.gcd_game import get_all_divisors


MAIN_GAME_QUESTION = ('Answer "yes" if given number is prime. \
Otherwise answer "no".')


def data():
    random_number = randint(1, 100)
    if random_number < 2:
        correct_answer = False or 'no'
    else:
        all_divisors = set(get_all_divisors(random_number))
        prime_divisors = {1, random_number}
        correct_answer = all_divisors.difference(prime_divisors) == set() and 'yes' or 'no'
    return random_number, correct_answer
