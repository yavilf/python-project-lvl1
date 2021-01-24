#!/usr/bin/env python
import prompt
from random import randint


def get_name():
    name = prompt.string('May I have your name? ')
    return name


def is_prime(number):
    for i in range(number):
        if i > 1:
            if number % i == 0:
                return 'no'

    return 'yes'


def prime_game():
    name = get_name()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    quantity_of_rounds = 3
    while quantity_of_rounds != 0:
        number = randint(1, 99)
        print('Question: {}'.format(number))
        answer = prompt.string('Your answer: ')
        if is_prime(number) == 'yes':
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
            break

    if quantity_of_rounds == 0:
        print('Congratulations, {}!'.format(name))
