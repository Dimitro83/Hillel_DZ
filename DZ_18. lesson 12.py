import csv
import json
import random

with open('name_age.json', 'r', encoding='utf-8') as f:
    dz_17 = json.load(f)

with open('name_age.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(['ID', 'Имя', 'Возраст', 'Телефон'])
    for key, name_age in dz_17.items():
        if random.random() <= 0.75:
            operators = ['095', '066', '098', '096', '050', '097']
            mobile = random.choice(operators) + ''.join([str(random.randint(0, 9)) for i in range(7)])
        writer.writerow([key, name_age[0], name_age[1], mobile])
