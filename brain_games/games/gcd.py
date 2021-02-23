#!/usr/bin/env python
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(number_1, number_2):
    if number_1 > number_2:
        while number_1 != 0 or number_2 != 0:
            number_1 = number_1 % number_2
            if number_1 == 0:
                return number_2
            number_2 = number_2 % number_1
            if number_2 == 0:
                return number_1
    elif number_2 > number_1:
        while number_1 != 0 or number_2 != 0:
            number_2 = number_2 % number_1
            if number_2 == 0:
                return number_1
            number_1 = number_1 % number_2
            if number_1 == 0:
                return number_2
    else:
        return number_1


def game_body():
    number_1 = randint(1, 99)
    number_2 = randint(1, 99)
    question = 'Question: {} {}'.format(number_1, number_2)
    check = gcd(number_1, number_2)

    return str(check), question
