#!/usr/bin/env python3


from random import randint


main_game_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
def get_all_divisors(number):
    divisors = []
    for i in range(1, int(number/2)+1):
        if number % i == 0:
            divisors.append(i)
    return divisors


def data():
    random_number = randint(1, 100)
    all_divisors = set(get_all_divisors(random_number))
    prime_divisors = {1, random_number}
    if all_divisors.difference(prime_divisors) == set():
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer
