#!/usr/bin/env python
from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for i in range(number):
        if i > 1:
            if number % i == 0:
                return 'no'

    return 'yes'


def game_body():
    number = randint(1, 99)
    question = 'Question: {}'.format(number)

    if is_prime(number) == 'yes':
        check = 'yes'
    else:
        check = 'no'

    return check, question
