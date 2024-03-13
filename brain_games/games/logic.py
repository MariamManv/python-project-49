import prompt
from random import randint
from random import choice


def hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


#для работы функции нужно будет объявить перменные:
#main_game_question с основным вопросом игры
#specific_game_question в формате Question: пример
#result -результат решения конретного примера
def common_logic():
    name = hello()
    print(f'{main_game_question}')
    count = 0
    while count < 3:
        #тут как-то ввести гору переменных для общей логики??
        print(f'{specific_game_question}')
        user_input = input(f"""Your answer: """)
        #тут идет сравнение с првильным ответом через if, которое непонятно как прописать переменными,
        #при этом если ответ правильный, то счетчик идет вверх
        count += 1
        print('Correct!')
            if count < 3:
                print('')
            else:
                print(f'Congratulations, {name}!)
        else:
            print(f"""{user_input} is wrong answer ;(. Correct answer was '{result}'.
Let's try again, {name}""")
            break
