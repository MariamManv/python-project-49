#!/usr/bin/env python3


from random import randint


main_game_question = 'Find the greatest common divisor of given numbers.'
def get_all_divisors(number):
    divisors = set()
    for i in range(1, number+1):
        if number % i == 0:
            divisors.add(i)
    return divisors

def data():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    given_numbers = (f'{random_number_1} {random_number_2}')
    divisors_num_1 = get_all_divisors(random_number_1)
    divisors_num_2 = get_all_divisors(random_number_2)
    common_divisors = divisors_num_1 & divisors_num_2
    max_divisor = max(common_divisors)
    correct_answer = str(max_divisor)
    return given_numbers, correct_answer
