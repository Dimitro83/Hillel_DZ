def check(number):
    if number.isdigit() and int(number) == 0:
        return "Вы ввели ноль",
    elif number.isdigit():
        return "Вы ввели положительное целое число:", number
    try:
        number_1 = int(number)
        if number_1 < 0:
            return 'Вы ввели отрицательное целое число:', number_1
    except:
        list1 = list(number)
        i = ','
        if i in list1:
            new_n_name = '.'
            list1 = [a if a != i else new_n_name for a in list1]
        try:
            number_2 = float(''.join(list1))
            if number_2 > 0:
                return 'Вы ввели положительное дробное число:', number_2
            else:
                return 'Вы ввели отрицательное дробное число:', number_2
        except:
            return 'Вы ввели не корректное число:', number


while True:
    user_answer = input('Введите число \n'
                   'или "выход", "exit", "quit", "e" или "q" для выхода: ')
    if user_answer.lower() in ("выход", "exit", "quit", "e", "q"):
        break
    else:
        result = check(user_answer)
        print(*result, '\n')
        continue
