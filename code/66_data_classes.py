class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1,2)
p2 = Point(1,2)
print(p1 == p2)
print(id(p1))
print*(id(p2))

from collections import namedtuple
Point = namedtuple("Point",["x", "y"])
P1 = Point(x=1, y=2)
P1 = Point(x=10, y=2)
P2 = Point(x=1, y=2)
print(P1 == P2)
