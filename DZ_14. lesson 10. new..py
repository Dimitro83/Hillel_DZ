def check(number):
    if number in ('0', '0.0', '0.00', '0.000', '.0', '.00', '.000'):
        return "Вы ввели ноль",
    elif number.isdigit():
        return "Вы ввели положительное целое число:", number
    elif number.startswith('-') and "." in number:
        if number.startswith('-.'):
            return "Вы ввели отрицательное дробное число:", number.replace('-.', '-0.')
        elif number.startswith('--'):
            return "Вы ввели не корректное число:", number
        else:
            return "Вы ввели отрицательное дробное число:", number
    elif number.startswith('-') and "," in number:
        if number.startswith('-,'):
            return "Вы ввели отрицательное дробное число:", number.replace('-,', '-0.')
        elif number.startswith('--'):
            return "Вы ввели не корректное число:", number
        else:
            return "Вы ввели отрицательное дробное число:", number.replace(',', '.')
    elif number.startswith('-'):
        if number.startswith('--'):
            return "Вы ввели не корректное число:", number
        else:
            return "Вы ввели отрицательное число:", number
    elif not number.isdigit():
        return "Вы ввели не корректное число:", number


while True:
    user_answer = input('Введите число \n'
                   'или "выход", "exit", "quit", "e" или "q" для выхода: ')
    if user_answer.lower() in ("выход", "exit", "quit", "e", "q"):
        break
    else:
        result = check(user_answer)
        print(*result, '\n')
        continue
