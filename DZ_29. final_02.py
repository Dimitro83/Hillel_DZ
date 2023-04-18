import json
import datetime


class Person:
    def __init__(self, name, surname, patronymic, birth_date, death_date, gender):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.birth_date = birth_date
        self.death_date = death_date
        self.gender = gender

    def validate_date(self, date):
        try:
            datetime.datetime.strptime(date, '%d.%m.%Y')
            return True
        except ValueError:
            return False

    def get_age(self):
        today = datetime.datetime.today()
        if self.death_date is None:
            age = today.year - datetime.datetime.strptime(self.birth_date, '%d.%m.%Y').year
            if today.month < datetime.datetime.strptime(self.birth_date, '%d.%m.%Y').month or \
                    (today.month == datetime.datetime.strptime(self.birth_date, '%d.%m.%Y').month
                     and today.day < datetime.datetime.strptime(self.birth_date, '%d.%m.%Y').day):
                age -= 1
        else:
            age = datetime.datetime.strptime(self.death_date, '%d.%m.%Y').year - datetime.datetime.strptime(
                self.birth_date, '%d.%m.%Y').year
            if datetime.datetime.strptime(self.death_date, '%d.%m.%Y').month < datetime.datetime.strptime(
                    self.birth_date, '%d.%m.%Y').month \
                    or (datetime.datetime.strptime(self.death_date, '%d.%m.%Y').month == datetime.datetime.strptime(
                    self.birth_date, '%d.%m.%Y').month
                        and datetime.datetime.strptime(self.death_date, '%d.%m.%Y').day < datetime.datetime.strptime(
                        self.birth_date, '%d.%m.%Y').day):
                age -= 1
        return age


class PeopleDatabase:
    def __init__(self):
        self.people_list = []

    def add_person(self, person):
        if isinstance(person, Person):
            self.people_list.append(person)
            return "Запись успешно добавлена."
        else:
            return "Неверный формат введённых данных."

    def find_person(self, name, surname, patronymic):
        result_list = []
        for person in self.people_list:
            if name and surname and patronymic:
                if (person.name.lower() == name.lower() and
                   person.surname.lower() == surname.lower() and
                   person.patronymic.lower() == patronymic.lower()):
                    result_list.append(person)
            elif name and surname:
                if (person.name.lower() == name.lower() and
                   person.surname.lower() == surname.lower()):
                    result_list.append(person)
            elif name:
                if person.name.lower() == name.lower():
                    result_list.append(person)
            else:
                return "Некорректный поисковый запрос."
        return result_list

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as outfile:
                json.dump(self.people_list, outfile, default=lambda o: o.__dict__)
            return "Данные успешно сохранены."
        except FileNotFoundError:
            return "Файл не найден."

    def load_from_file(self, filename):
        try:
            with open(filename) as json_file:
                data = json.load(json_file)
            self.people_list = [Person(**person) for person in data]
            return "Данные успешно загружены."
        except FileNotFoundError:
            return "Файл не найден."


def main():
    people_database = PeopleDatabase()
    while True:
        print("1. Добавить новую запись")
        print("2. Найти запись")
        print("3. Сохранить данные в файл")
        print("4. Загрузить данные из файла")
        print("5. Выход")
        try:
            choice = int(input("Выберите пункт меню: "))
        except ValueError:
            print("Некорректные данные.")
            continue

        if choice == 1:
            name = input("Введите имя: ")
            surname = input("Введите фамилию: ")
            patronymic = input("Введите отчество: ")
            while True:
                birth_date = input("Введите дату рождения в формате дд.мм.гггг: ")
                if Person.validate_date(Person, birth_date):
                    break
                else:
                    print("Некорректные данные.")

            death_date = input("Введите дату смерти в формате дд.мм.гггг (если применимо): ")
            if death_date:
                while True:
                    if Person.validate_date(Person, death_date):
                        break
                    else:
                        print("Некорректные данные.")

            gender = input("Введите пол (мужской/женский): ")
            person = Person(name, surname, patronymic, birth_date, death_date, gender)
            print(people_database.add_person(person))

        elif choice == 2:
            name = input("Введите имя: ")
            surname = input("Введите фамилию: ")
            patronymic = input("Введите отчество: ")
            people_list = people_database.find_person(name, surname, patronymic)
            print(people_list)

        elif choice == 3:
            filename = input("Введите имя файла: ")
            print(people_database.save_to_file(filename))

        elif choice == 4:
            filename = input("Введите имя файла: ")
            print(people_database.load_from_file(filename))

        elif choice == 5:
            break

        else:
            print("Некорректный пункт меню.")


if __name__ == "__main__":
    main()
