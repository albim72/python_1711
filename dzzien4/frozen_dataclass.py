from dataclasses import dataclass
import dis

@dataclass(frozen=True, order=False)
class Point:
    x: int
    y: int

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __lt__(self, other:"Point") -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return self.length() < other.length()

    # def set_x(self,nx):
    #     self.x = nx

p1 = Point(3, 4)
p2 = Point(2, 12)
p3 = Point(10, 1)


points = [p1, p2, p3]
#sortowanie po długości nie naruszając porządku dataclass
by_length = sorted(points, key=lambda p: p.length())
for p in by_length:
    print(f"{p.x} {p.y} -> length -> {p.length():.2f}")

print(p1.length())
print(p2.length())

# p1.set_x(10)

print(p1 < p2)
print(p1 > p2)

print("++++++++++  dis -> Point +++++++++++")
dis.dis(Point.__init__)


