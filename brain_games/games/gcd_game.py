from random import randint


MAIN_GAME_QUESTION = 'Find the greatest common divisor of given numbers.'


def find_gcd(num1, num2):
    divisors_1 = set()
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            divisors_1.add(i)
    divisors_2 = set()
    for i in range(1, num2 + 1):
        if num2 % i == 0:
            divisors_2.add(i)
    common_divisors = divisors_1 & divisors_2
    max_divisor = max(common_divisors)
    return max_divisor


MIN_NUMBER = 1
MAX_NUMBER = 100


def create_data():
    random_number_1 = randint(MIN_NUMBER, MAX_NUMBER)
    random_number_2 = randint(MIN_NUMBER, MAX_NUMBER)
    max_divisor = find_gcd(random_number_1, random_number_2)
    correct_answer = str(max_divisor)
    return (f'{random_number_1} {random_number_2}'), correct_answer
