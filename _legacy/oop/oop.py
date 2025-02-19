import math
class shape:
    def __init__(self):
        pass
    def area(self):
        pass
class circle(shape):
    def __init__(self, r):
        shape.__init__(self)
        self._radius = r
    def area(self):
        return self._radius * self._radius * math.pi
class rectangle(shape):
    def __init__(self, side1, side2):
        shape.__init__(self)
        self._a = side1
        self._b = side2
    def area(self):
        return self._a * self._b
class square(shape):
    def __init__(self, side):
        shape.__init__(self)
        self._side = side
    def area(self):
        return self._side ** 2

sq = square(4)
cir = circle(7)
rect = rectangle(3,6)
print(sq.area())
print(cir.area())
print(rect.area())