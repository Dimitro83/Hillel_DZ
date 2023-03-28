user_1 = input("please enter something 1: ")
user_2 = input("please enter something 2: ")
user_3 = input("please enter something 3: ")
user_4 = input("please enter something 4: ")

file = open('DZ_16.txt', 'w')
file.write(f'{user_1}\n{user_2}\n')
file.close()
with open('DZ_16.txt', 'a') as file:
    file.write(f'{user_3}\n{user_4}')
