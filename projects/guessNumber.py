import random


def guess_number(x):
    print('======================')
    print(' Welcome to the Game! ')
    print('======================')

    print(f'Select a number between 1 and {x} for the pc to try guess it!')

    lower_limit = 1
    upper_limit = x
    response = ''

    while response != 'c':
        if lower_limit != upper_limit:
            prediction = random.randint(lower_limit, upper_limit)
        else:
            prediction = lower_limit

        response = input(
            f'My prediction is {prediction}. If higher, write (A). If lower, write (B). If it is correct, write (C): ').lower()

        if response == 'a':
            upper_limit = prediction - 1
        elif response == 'b':
            lower_limit = prediction + 1

    print(
        f'Yeah!, The computer guessed your number successfully: {prediction}')


guess_number(10)
