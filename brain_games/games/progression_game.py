from random import randint
from random import choice


MAIN_GAME_QUESTION = 'What number is missing in the progression?'
MIN_NUMBER = 1
MAX_NUMBER = 100
MIN_STEP_NUMBER = 1
MAX_STEP_NUMBER = 15
COUNT = 10


def create_data():
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    step = randint(MIN_STEP_NUMBER, MAX_STEP_NUMBER)
    progression = list(range(first_number, first_number + COUNT * step, step))
    correct_index = choice(range(len(progression)))
    correct_answer = str(progression[correct_index])
    progression[correct_index] = '..'
    finished_progression = ' '.join([str(num) for num in progression])
    return finished_progression, correct_answer
