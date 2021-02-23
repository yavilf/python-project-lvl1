#!/usr/bin/env python
from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'


def game_body():
    number_1 = randint(1, 99)
    number_2 = randint(1, 99)
    sign = choice('+-*')
    question = 'Question: {} {} {}'.format(number_1, sign, number_2)

    if sign == '+':
        check = number_1 + number_2
    elif sign == '-':
        check = number_1 - number_2
    else:
        check = number_1 * number_2

    return str(check), question
