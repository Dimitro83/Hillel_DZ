import random
from datetime import datetime


def decorator_time(func):
    def wrapper(*args, **kwargs):
        now = datetime.now()
        print("Function start and....")
        func(*args, **kwargs)
        time_spend = datetime.now() - now
        print(f"....time spend: {time_spend}\n")
    return wrapper


@decorator_time
def list_built(a):
    num_list = 0
    list_1 = []
    while num_list < a:
        num = random.randint(1, 100)
        list_1.append(num)
        num_list += 1
    print(list_1)
    return list_1


@decorator_time
def list_change(b):
    output = [i.upper() for i in b if i.upper() == i[::-1].upper()]
    print(f'old list: {b}')
    print(f'new list: {output}')


quantity = 10000
input_data = ['hello', 'Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык', 'day', 'night', 'qwerrewq', 'rain']

list_built(quantity)
list_change(input_data)
