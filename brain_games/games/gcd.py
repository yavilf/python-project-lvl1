#!/usr/bin/env python
import prompt
from random import randint


def get_name():
    name = prompt.string('May I have your name? ')
    return name


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


def gcd_game():
    name = get_name()
    print('Find the greatest common divisor of given numbers.')
    quantity_of_rounds = 3
    while quantity_of_rounds != 0:
        number_1 = randint(1, 99)
        number_2 = randint(1, 99)
        print('Question: {} {}'.format(number_1, number_2))
        answer = prompt.string('Your answer: ')
        check = gcd(number_1, number_2)

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
