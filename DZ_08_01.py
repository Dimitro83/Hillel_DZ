import random
while True:
    your_list = input('please enter how many items in list do you want: ')
    if not your_list.isdigit():
        continue
    else:
        break

quantity_list = 0
worklist = []
while quantity_list < int(your_list):
    numbers = random.randint(1, 10)
    worklist.append(numbers)
    quantity_list += 1
print(worklist)


def counter(a):
    target = a
    index = 0
    quantity = 0
    list_final = []
    for i in worklist:
        if int(i) == target:
            quantity += 1
        index += 1
# хотел чтоб здесь list_final получался из сложенных list_01, а потом уже создать словарь.
# я вообще в правильном направлении???
    # print(numero)
    # print(quantity)
    # list_final = (numero) + (quantity)
        list_01 = [numero, quantity]
        list_final += list_01
    # print(dict_final)
    print(list_01)
    print(list_final)


numero = 1
for q in range(1, 11):
    counter(numero)
    numero += 1
