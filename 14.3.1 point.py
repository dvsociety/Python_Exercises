def valid_number(number):
    if not isinstance(number,(int,float)):
        raise Exception(f"{number} no es un numero ")
    return number

class Point:

    def __init__(self, x, y):
        self.x = valid_number(x)
        self.y = valid_number(y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self): 
        return f"Punto({self.x}. {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance(self, other):
        return self.__sub__(other).norm()

point1 = Point(2,3)
point2 = Point(4,4)
print(point1 - point2)
print(point1.distance(point2))
