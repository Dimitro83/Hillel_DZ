class Calculator(object):

    def __init__(self):
        pass

    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def division(self, num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            print('You can not divide by zero!')
            return 0

    def multiplication(self, num1, num2):
        return num1 * num2

    def power(self, num1, num2):
        try:
            if num2 < 0:
                raise NegativePowerError(f'You can not raise a number to a negative power. num1: {num1}, num2: {num2}')
            return num1 ** num2
        except NegativePowerError as err:
            print(err)
            return 0

    def square_root(self, num):
        try:
            if num < 0:
                raise NegativeSquareRootError(f'You can not calculate the square root of a negative number. num: {num}')
            return num ** 0.5
        except NegativeSquareRootError as err:
            print(err)
            return 0


class NegativePowerError(Exception):
    pass


class NegativeSquareRootError(Exception):
    pass


calc = Calculator()
while True:
    try:
        first_num = float(input('Enter the first number: '))
        second_num = float(input('Enter the second number: '))
        operator = input('Enter the operation (+, -, *, /, **, SQRT): ')
        if operator == '+':
            print(calc.addition(first_num, second_num))
        elif operator == '-':
            print(calc.subtraction(first_num, second_num))
        elif operator == '*':
            print(calc.multiplication(first_num, second_num))
        elif operator == '/':
            print(calc.division(first_num, second_num))
        elif operator == '**':
            print(calc.power(first_num, second_num))
        elif operator == 'SQRT':
            print(calc.square_root(first_num))
        else:
            print("Please enter a valid operator.")
    except ValueError:
        print("Please enter valid numbers.")
        