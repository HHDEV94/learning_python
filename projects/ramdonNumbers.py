import random


def adivina_el_numero(x):
    print('========================')
    print('  Welcome to the game!  ')
    print('========================')

    randomNumber = random.randint(1, x)
    prediction = 0

    while prediction != randomNumber:
        prediction = int(
            input(f'Guess the number between 1 and {x}: '))  # f-string

        if prediction < randomNumber:
            print('Try again. This number is tiny.')
        elif prediction > randomNumber:
            print('Try again. This number is big.')

    print(f'Congratulations! You guess the number {x} successfully!')


adivina_el_numero(15)
