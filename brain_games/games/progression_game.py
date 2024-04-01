from random import randint
from random import choice


RULES_OF_THE_GAME = 'What number is missing in the progression?'
MIN_INITIAL_TERM_NUMBER = 1
MAX_INITIAL_TERM_NUMBER = 100
MIN_COMMON_DIFFERENCE_NUMBER = 1
MAX_COMMON_DIFFERENCE_NUMBER = 15
COUNT = 10


def get_question_and_correct_answer():
    initial_term = randint(MIN_INITIAL_TERM_NUMBER, MAX_INITIAL_TERM_NUMBER)
    common_difference = (
     randint(MIN_COMMON_DIFFERENCE_NUMBER, MAX_COMMON_DIFFERENCE_NUMBER))
    progression = (
        list(range(initial_term, initial_term + COUNT 
    * common_difference, common_difference)))
    correct_index = choice(range(len(progression)))
    correct_answer = str(progression[correct_index])
    progression[correct_index] = '..'
    finished_progression = ' '.join([str(num) for num in progression])
    return finished_progression, correct_answer
