import prompt


def get_name():
    name = prompt.string('May I have your name? ')
    return name


def engine(game):
    print('Welcome to the Brain Games!')
    name = get_name()
    print(game.DESCRIPTION)
    QUANTITY_OF_ROUNDS = 3
    while QUANTITY_OF_ROUNDS != 0:
        check, question = game.game_body
        print(question)
        answer = prompt.string('Your answer: ')
        if answer == check:
            print('Correct!')
            QUANTITY_OF_ROUNDS -= 1
        else:
            print("'{}', is wrong answer ;(. "
                  "Correct answer was '{}'".format(answer, check))
            print("Let's try again, {}!".format(name))
            return

    print('Congratulations, {}!'.format(name))
