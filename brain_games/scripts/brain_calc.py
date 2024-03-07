#!/usr/bin/env python3


import prompt
from random import randint
from random import choice


def hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def main():
    name = hello()
    print('What is the result of the expression?')
    count = 0
    while count < 3:
        random_number_1 = randint(1, 100)
        random_number_2 = randint(1, 100)
        operations = ['+', '-', '*']
        random_operation = choice(operations)
        print(f"""Question:{random_number_1} {random_operation} {random_number_2}""")
        user_input = input(f"""Your answer: """)
        if random_operation == '+':
            result = random_number_1 + random_number_2
        elif random_operation == '-':
            result = random_number_1 - random_number_2
        else:
            result = random_number_1 * random_number_2
        if int(user_input) == result:
            count += 1
            print('Correct!')
            if count <3:
                print('')
            else:
                print(f'Congratulations, {name}!')
        else:
            print(f"""'{user_input}' is wrong answer ;(. Correct answer was '{result}'.
Let's try again, {name}""")
            break


if __name__ == '__main__':
    main()

