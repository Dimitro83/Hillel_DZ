class Auto:

    def __init__(self, brand, age, mark, weight=700, color='white'):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.weight = weight
        self. color = color

    def move(self):
        print('move')

    def birthday(self):
        self.age += 1
        print(self.age)

    def stop(self):
        print('stop')
