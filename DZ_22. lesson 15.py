import math


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)


class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

# переопределил метод __str__ чтоб выводился на печать сначала радиус, а потом координаты
    def __str__(self):
        return f'( radius={self.radius}, ' + super().__str__()[1:]

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        radius = self.radius + other.radius
        return Circle(radius, x, y)

# домашка 22
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        radius = abs(self.radius - other.radius)
        return Circle(radius, x, y) if radius != 0 else Point(x, y)

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius**2)


c_1 = Circle(10, 13, 2)
c_2 = Circle(15, 2, 3)
c_3 = Circle(10)
print("Circle c_1: ", c_1)
print("Circle c_2: ", c_2)
print("Circle c_3: ", c_3)
print("Circle c_1 - c_2: ", c_1 - c_2)
print("Circle c_1 - c_3: ", c_1 - c_3)
