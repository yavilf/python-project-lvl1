#!/usr/bin/env python
from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def get_progression():
    progression_length = randint(5, 10)
    first_number_in_progression = randint(1, 100)
    step = randint(1, 10)
    progression = []
    for i in range(progression_length):
        term_of_progression = first_number_in_progression + (step * i)
        progression.append(term_of_progression)
    return progression


def game_body():
    progression = get_progression()
    secret_number = randint(1, len(progression) - 1)
    check = progression[secret_number]

    progression[secret_number] = '..'

    question = 'Question:'
    for i in progression:
        question += ' ' + str(i)

    return str(check), question
