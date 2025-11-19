import math
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self, ax):
        """Rysuje kształt na podanym obiekcie axes."""
        pass

    def msg(self, info):
        return f"I am {self.__class__.__name__} and my area is {self.area():.2f}. {info}"


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def draw(self, ax):
        square = patches.Rectangle(
            (0, 0),            # lewy dół
            self.side,         # szerokość
            self.side,         # wysokość
            fill=False,
            linewidth=3,
            edgecolor="blue"
        )
        ax.add_patch(square)
        ax.set_xlim(-1, self.side + 1)
        ax.set_ylim(-1, self.side + 1)
        ax.set_aspect("equal", adjustable="box")
        ax.set_title("Square")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def draw(self, ax):
        circle = patches.Circle(
            (0, 0),           # środek
            self.radius,      # promień
            fill=False,
            linewidth=3,
            edgecolor="red"
        )
        ax.add_patch(circle)
        ax.set_xlim(-self.radius - 1, self.radius + 1)
        ax.set_ylim(-self.radius - 1, self.radius + 1)
        ax.set_aspect("equal", adjustable="box")
        ax.set_title("Circle")


# ---- DEMO ----

kw = Square(4)
cr = Circle(6)

print(kw.msg("to jest mój kwadrat!"))
print(cr.msg("to jest moje koło!"))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

kw.draw(ax1)
cr.draw(ax2)

plt.show()
