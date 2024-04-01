import prompt


ROUND_NUMBER = 3


def execute_brain_games(specific_game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(specific_game.RULES_OF_THE_GAME)
    count = 0
    while count < ROUND_NUMBER:
        question, correct_answer = specific_game.get_question_and_correct_answer()
        print(f'Question: {question}')
        user_input = input('Your answer: ')
        if user_input == correct_answer:
            count += 1
            print('Correct!')
            if count == ROUND_NUMBER:
                print(f'Congratulations, {name}!')
        else:
            print(f"{user_input} is wrong answer ;(. \
Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            break
