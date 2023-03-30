from random import randint
import json

name_1 = "Vasil"
name_2 = "Петя"
name_3 = "Коля"
name_4 = "Alex"
name_5 = "Жора"
age_1 = 15
age_2 = 35
age_3 = 27
age_4 = 65
age_5 = 54

list_name = [name_1, name_2, name_3, name_4, name_5]
list_age = [age_1, age_2, age_3, age_4, age_5]

name_age = {randint(100000, 999999): (name, age) for name, age in zip(list_name, list_age)}
print(name_age)

with open('name_age.json', 'w') as file:
    json.dump(name_age, file)
