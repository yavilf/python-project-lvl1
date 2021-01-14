#!/usr/bin/env python
import prompt
from random import randint


def get_name():
    name = prompt.string('May I have your name? ')
    return name


def is_even(number):
    return number % 2 == 0


def even_game():
    name = get_name()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    quantity_of_rounds = 3
    while quantity_of_rounds != 0:
        number = randint(1, 99)
        print('Question: {}'.format(number))
        answer = prompt.string('Your answer: ')
        if is_even(number):
            check = 'yes'
        else:
            check = 'no'

        if answer == check:
            print('Correct!')
            quantity_of_rounds -= 1
        else:
            print("'{}', is wrong answer ;(. "
                  "Correct answer was '{}'".format(answer, check))
            print("Let's try again, {}!".format(name))
            quantity_of_rounds = 3

    print('Congratulations, {}!'.format(name))