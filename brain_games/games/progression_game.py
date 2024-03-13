#!/usr/bin/env python3


from random import randint
from random import choice


main_game_question = 'What number is missing in the progression?'


def data():
    first_number = randint(1, 100)
    step = randint(1,15)
    count = 10 #количество чисел в прогрессии
    progression = list(range(first_number, first_number + count * step, step ))
    correct_index = choice(range(len(progression)))
    correct_answer = str(progression[correct_index])
    progression[correct_index] = '. .'
    finished_progression = ' '.join([str(num) for num in progression])
    return finished_progression, correct_answer
