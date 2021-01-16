#!/usr/bin/env python
import prompt
from random import randint, choice


def get_name():
    name = prompt.string('May I have your name? ')
    return name


def calc_game():
    name = get_name()
    print('What is the result of the expression?')
    quantity_of_rounds = 3
    while quantity_of_rounds != 0:
        number_1 = randint(1, 99)
        number_2 = randint(1, 99)
        sign = choice('+-*')
        print('Question: {} {} {}'.format(number_1, sign, number_2))
        answer = prompt.string('Your answer: ')

        if sign == '+':
            check = number_1 + number_2
        elif sign == '-':
            check = number_1 - number_2
        else:
            check = number_1 * number_2

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
