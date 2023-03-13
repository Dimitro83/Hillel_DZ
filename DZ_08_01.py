import random
while True:
    your_list = input('please enter how many items in list do you want, but not more than 200: ')
    if not your_list.isdigit() or int(your_list) == 0 or int(your_list) > 200:
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
print('_'*50)


def counter(lst, dct_temp):
    for i in lst:
        if i in dct_temp:
            dct_temp[i] += 1
        else:
            dct_temp[i] = 1


dct_result = {}

counter(worklist, dct_result)
print(dct_result)
print('_'*50)
end_world = lambda item: 'раза' if dct_result[item] in \
                                   (2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64,
                                    72, 73, 74, 82, 83, 84, 92, 93, 94, 102, 103, 104, 122, 123, 124,
                                    132, 133, 134, 142, 143, 145, 152, 153, 154, 162, 163, 164,
                                    172, 173, 174, 182, 183, 184, 192, 193, 194) else 'раз'

for item in sorted(dct_result):
    print(f'число %d встречается в первоначальном списке %d {end_world(item)}' % (item, dct_result[item]))
