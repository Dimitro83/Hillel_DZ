while True:
    number = input('To check "Even" or "Odd" or "Zero", please enter a number: ')
    if not number.isdigit():
        continue
    else:
        break


result = lambda number: print(f'Number {number} is ZERO') if int(number) == 0\
    else print(f'Number {number} is EVEN') if int(number) % 2 == 0 \
    else print(f'Number {number} is ODD')
result(number)
