#!/usr/bin/env python
from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def game_body():
    number = randint(1, 99)
    question = 'Question: {}'.format(number)

    if is_even(number):
        check = 'yes'
    else:
        check = 'no'

    return check, question
