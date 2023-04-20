'''1. wap class named as circle with attribute radius and two methods that will compute the area and perimeter of the circle.'''
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14
    def perimeter(self):
        return 2 * self.pi * self.radius 
    def area(self):
        return self.pi * self.radius * self.radius

circle = Circle(5)
print('perimeter of circle:', circle.perimeter())
print('area of circle:', circle.area())