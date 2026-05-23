import math

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Le rayon ne peut pas être négatif.")
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        if value < 0:
            raise ValueError("Le diamètre ne peut pas être négatif.")
        self._radius = value / 2

    @property
    def area(self):
        return math.pi * (self._radius ** 2)

    def __repr__(self):
        return f"Circle(radius={self._radius})"

    def __str__(self):
        return f"Cercle de rayon {self._radius} (Diamètre: {self.diameter}, Aire: {self.area:.2f})"

    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(self._radius + other._radius)

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius == other._radius

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius < other._radius

    def __le__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius <= other._radius