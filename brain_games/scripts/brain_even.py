#!/usr/bin/env python3


import prompt
from random import randint


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def main():
    name = hello()
    print('Answer \"yes\" if the number is even, otherwise answer \"no\".')
    count = 0
    while count < 3:
        random_number = randint(1, 1000)
        print(f"""Question:{random_number} """)
        user_input = input(f"""Your answer: """)
        if (user_input.lower() == 'yes' and random_number % 2 == 0) or (user_input.lower() == 'no' and random_number % 2 != 0):
            count += 1
            print('Correct!')
            if count < 3:
                print('')
            else:
                print(f'Congratulations, {name}!')
        else:
            if random_number % 2 == 0:
                answer = 'yes'
            else:
                answer = 'no'
            print(f"""'{user_input}' is wrong answer ;(. Correct answer was '{answer}'.
Let's try again, {name}""")
            break


if __name__ == '__main__':
    main()
