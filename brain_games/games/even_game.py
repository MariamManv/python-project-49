#!/usr/bin/env python3
from random import randint


main_game_question = 'Answer "yes" if the number is even, otherwise answer "no".'
def data():
    random_number = randint(1, 1000)
    if random_number % 2 == 0:
       correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer
