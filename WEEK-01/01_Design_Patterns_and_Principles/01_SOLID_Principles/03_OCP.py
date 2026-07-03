# Open/Closed Principle (OCP)

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


rectangle = Rectangle(10, 5)
circle = Circle(7)

print("Rectangle Area:", rectangle.area())
print("Circle Area:", round(circle.area(), 2))