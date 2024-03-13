#!/usr/bin/env python3


import prompt
from random import randint
from random import choice


main_game_question = 'What is the result of the expression?'
def data():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    operations = ['+', '-', '*']
    random_operation = choice(operations)
    equation = (f'{random_number_1} {random_operation} {random_number_2}')
    if random_operation == '+':
        correct_answer = random_number_1 + random_number_2
    elif random_operation == '-':
        correct_answer = random_number_1 - random_number_2
    else:
        correct_answer = random_number_1 * random_number_2
    return equation, correct_answer
