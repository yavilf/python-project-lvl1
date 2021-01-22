#!/usr/bin/env python
import prompt
from random import randint


def get_name():
    name = prompt.string('May I have your name? ')
    return name


def get_progression():
    progression_length = randint(5, 10)
    first_number_in_progression = randint(1, 100)
    step = randint(1, 10)
    progression = []
    for i in range(progression_length):
        term_of_progression = first_number_in_progression + (step * i)
        progression.append(term_of_progression)
    return progression


def progression_game():
    name = get_name()
    print('What number is missing in the progression?')
    quantity_of_rounds = 3
    while quantity_of_rounds != 0:
        progression = get_progression()
        secret_number = randint(1, len(progression) - 1)
        check = progression[secret_number]

        for i in range(len(progression)):
            if i == secret_number:
                progression[i] = '..'

        print('Question:', end='\t')
        for i in progression:
            print(i, end='\t')
        print()
        answer = prompt.string('Your answer: ')

        if answer == str(check):
            print('Correct!')
            quantity_of_rounds -= 1
        else:
            print("'{}', is wrong answer ;(. "
                  "Correct answer was '{}'".format(answer, check))
            print("Let's try again, {}!".format(name))
            break

    if quantity_of_rounds == 0:
        print('Congratulations, {}!'.format(name))
