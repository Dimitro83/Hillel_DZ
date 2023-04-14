import json
import datetime


# функция для вычисления возраста человека
def get_age(birth_date, death_date=None):
    today = datetime.date.today()
    if death_date is None:
        age = today.year - birth_date.year
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
    else:
        age = death_date.year - birth_date.year
        if death_date.month < birth_date.month or (death_date.month == birth_date.month and death_date.day < birth_date.day):
            age -= 1
    return age


# функция для записи данных в файл
def save_data(data):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)


# функция для загрузки данных из файла
def load_data():
    with open('data.json') as json_file:
        data = json.load(json_file)
    return data


# функция для добавления новых записей
def add_record(data):
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    birth_date = input('Введите дату рождения в формате ДД.ММ.ГГГГ: ')
    birth_date = datetime.datetime.strptime(birth_date, '%d.%m.%Y').date()
    gender = input('Введите пол (мужской или женский): ').lower()
    while gender not in ('мужской', 'женский'):
        gender = input('Введите пол (мужской или женский): ').lower()
    death_date = input('Введите дату смерти в формате ДД.ММ.ГГГГ (если неизвестно, нажмите Enter): ')
    if death_date:
        death_date = datetime.datetime.strptime(death_date, '%d.%m.%Y').date()
    data.append({
        'name': name,
        'surname': surname,
        'patronymic': patronymic,
        'birth_date': birth_date,
        'gender': gender,
        'death_date': death_date
    })


# функция для поиска записей
def find_record(data):
    search_string = input('Введите поисковый запрос: ').lower()
    for record in data:
        if search_string in record['name'].lower() or search_string in record['surname'].lower() or search_string in record['patronymic'].lower():
            print('ФИО: {} {} {}'.format(record['name'], record['surname'], record['patronymic']))
            print('Дата рождения: {}'.format(record['birth_date']))
            print('Пол: {}'.format(record['gender']))
            age = get_age(record['birth_date'], record['death_date'])
            print('Возраст: {}'.format(age))
            if record['death_date']:
                print('Дата смерти: {}'.format(record['death_date']))
            print('\n')


# функция для вывода меню
def show_menu():
    print('1. Загрузка данных из файла')
    print('2. Сохранение данных в файл')
    print('3. Добавление новой записи')
    print('4. Поиск')
    print('5. Выход')
    option = input('Выберите пункт меню: ')
    return option


data = []
option = ''
while option != '5':
    option = show_menu()
    if option == '1':
        data = load_data()
    elif option == '2':
        save_data(data)
    elif option == '3':
        add_record(data)
    elif option == '4':
        find_record(data)
