import prompt


def execute_brain_games(specific_game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(specific_game.MAIN_GAME_QUESTION)
    count = 0
    while count < 3:
        game_data = specific_game.create_data()
        print(f'Question: {game_data[0]}')
        user_input = input('Your answer: ')
        if user_input == game_data[1]:
            count += 1
            print('Correct!')
            if count == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"{user_input} is wrong answer ;(. \
Correct answer was '{game_data[1]}'.\nLet's try again, {name}!")
            break
