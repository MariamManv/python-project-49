from random import randint
from random import choice


MAIN_GAME_QUESTION = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 100


def create_data():
    random_number_1 = randint(MIN_NUMBER, MAX_NUMBER)
    random_number_2 = randint(MIN_NUMBER, MAX_NUMBER)
    operations = ['+', '-', '*']
    random_operation = choice(operations)
    if random_operation == '+':
        correct_answer = str(random_number_1 + random_number_2)
    elif random_operation == '-':
        correct_answer = str(random_number_1 - random_number_2)
    else:
        correct_answer = str(random_number_1 * random_number_2)
    return (
        f'{random_number_1} {random_operation} {random_number_2}'), correct_answer
