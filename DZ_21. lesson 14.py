import time


class Auto:

    def __init__(self, brand, age, mark, weight=700, color='white'):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.weight = weight
        self. color = color

    def move(self):
        print('move', end=' ')

    def birthday(self):
        self.age += 1
        print('birthday: ', self.age)

    def stop(self):
        print('stop')


class Truck(Auto):

    def __init__(self, brand, age, mark, max_load, weight=700, color='white'):
        super().__init__(brand, age, mark, weight, color)
        self.max_load = max_load

    def move(self):
        print('attention', end=' ')
        super().move()

    def load(self):
        time.sleep(1)
        print()
        print('load')
        time.sleep(1)


class Car(Auto):

    def __init__(self, brand, age, mark, max_speed, weight=700, color='white'):
        super().__init__(brand, age, mark, weight, color)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'max speed is {self.max_speed}')


truck_1 = Truck('Hyundai', 5, 'HD 120', 7000)
truck_2 = Truck('tesla', 1, 'Semi', 36000, color='black')
car_1 = Car('Toyota', 3, 'Rav4', 230)
car_2 = Car('Audi', 3, 'A3', 100, weight=1000)

print(f"Truck_1: {truck_1.brand}; Age: {truck_1.age}; Mark: {truck_1.mark}; "
      f"Max_load: {truck_1.max_load}; Weight: {truck_1.weight}; Color: {truck_1.color}")
truck_1.move()
truck_1.load()
truck_1.birthday()
truck_1.stop()
print("*"*100)

print(f"Truck_2: {truck_2.brand}; Age: {truck_2.age}; Mark: {truck_2.mark}; "
      f"Max_load: {truck_2.max_load}; Weight: {truck_2.weight}; Color: {truck_2.color}")
truck_2.move()
truck_2.load()
truck_2.birthday()
truck_2.stop()
print("*"*100)

print(f"Car_1: {car_1.brand}; Age: {car_1.age}; Mark: {car_1.mark}; "
      f"Max_speed: {car_1.max_speed}; Weight: {car_1.weight}; Color: {car_1.color}")
car_1.move()
car_1.birthday()
car_1.stop()
print("*"*100)

print(f"Car_2: {car_2.brand}; Age: {car_2.age}; Mark: {car_2.mark}; "
      f"Max_speed: {car_2.max_speed}; Weight: {car_2.weight}; Color: {car_2.color}")
car_2.move()
car_2.birthday()
car_2.stop()
print("*"*100)
