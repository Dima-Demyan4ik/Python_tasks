from math import pi
class Circle:
    @staticmethod
    def area(radius):
        return f"площадь равна {2*pi*radius}"
    def __init__(self, radius):
        self.radius=radius
a=Circle(65465465)
print(a.area(5))