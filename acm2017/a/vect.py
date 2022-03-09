import math


class Vect:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_point(self, v):
        return Vect(v.x - self.x, v.y - self.y)

    def dot(self, v):
        return self.x * v.x + self.y * v.y;

    def mag(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
