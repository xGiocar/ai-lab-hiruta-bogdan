from math import pi

class GeometricForm:
    def __init__(self):
        pass

    def getArea(self):
        return None

    def getPerimeter(self):
        return None


class Rectangle(GeometricForm):
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def getArea(self):
        return self.length * self.height

    def getPerimeter(self):
        return 2 * (self.length + self.height)


class Circle(GeometricForm):
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return round(pi * self.radius ** 2, 2)

    def getPerimeter(self):
        return round(2 * pi * self.radius, 2)

r = Rectangle(20, 2)
c = Circle(31)

print(r.getPerimeter())
print(r.getArea())
print(c.getPerimeter())
print(c.getArea())