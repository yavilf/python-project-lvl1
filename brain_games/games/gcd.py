#!/usr/bin/env python
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(number_1, number_2):
    while number_1 != 0 and number_2 != 0:
        if number_1 > number_2:
            number_1 %= number_2
        else:
            number_2 %= number_1
    return number_1 + number_2


def game_body():
    number_1 = randint(1, 99)
    number_2 = randint(1, 99)
    question = 'Question: {} {}'.format(number_1, number_2)
    check = gcd(number_1, number_2)

    return str(check), question
