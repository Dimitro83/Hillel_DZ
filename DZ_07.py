import random


def easy_game(secret_num, name):
    guess = 1
    while guess <= 5:
        number = input('  Try to guess: ')
        if not number.isdigit() or int(number) > 15:
            print(f'    "{number}" does not as requested. '
                  f'Enter a number between 0 and 15 included.')
            continue
        elif int(number) == secret_num:
            print(f'{name.title()}, You WIN!!!')
            break
        elif guess == 5:
            print('You LOOS')
        elif int(number) > secret_num:
            print(f'Guessed number is less. Remain {5 - guess} tries')
        elif int(number) < secret_num:
            print(f'Guessed number is more. Remain {5 - guess} tries')
        else:
            print(f'Remain {5 - guess} tries')
        guess += 1


def hard_game(secret_num, name):
    guess = 1
    while guess <= 2:
        number = input('  Try to guess: ')
        if not number.isdigit() or int(number) > 15:
            print(f'    "{number}" does not as requested. '
                  f'Enter a number between 0 and 15 included.')
            continue
        elif int(number) == secret_num:
            print(f'{name.title()}, You WIN!!!')
            break
        elif guess == 2:
            print('You LOOS')
        elif int(number) > secret_num:
            print(f'Guessed number is less. Remain {2 - guess} tries')
        elif int(number) < secret_num:
            print(f'Guessed number is more. Remain {2 - guess} tries')
        else:
            print(f'Remain {2 - guess} tries')
        guess += 1


secret = random.randint(0, 15)
print(secret)

player = input("Hello, what is you name?: ")
print(f'{player.title()}, lets play. I guessed a NUMBER from 0 to 15')
while True:
    difficulty = input('Please choose a difficulty.\n '
                       'Enter 1 for EASY or 2 for HARD: ')
    if not difficulty.isdigit() or int(difficulty) == 0 \
            or int(difficulty) > 2:
        print('Read again')
        continue
    elif int(difficulty) == 1:
        easy_game(secret, player)
    else:
        hard_game(secret, player)
    break
