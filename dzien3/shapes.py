import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def msg(self,info):
        return f"I am {self.__class__.__name__} and my area is {self.area()}. {info}"


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


kw = Square(4)
print(kw.msg("to jest mój kwadrat!"))

cr = Circle(6.7)
print(cr.msg("to jest moje koło!"))

