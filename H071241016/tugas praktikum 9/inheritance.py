class Shape:
    def __init__(self, color):
        self.color = color

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):                                   
        return self.width * self.height

class Circle(Shape):
    def __init__(self, color, radius, pi):
        super().__init__(color)
        self.radius = radius
        self.pi = pi

    def area(self):
        return self.pi * self.radius * self.radius
    
class Trapesium(Shape):
    def __init__(self, color,a , b, c, t):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c
        self.t = t

    def area(self):
        return self.a *  (self.b + self.c) * self.t

rect = Rectangle("red", 5, 10)
circle = Circle("blue", 5, 3.14)
trapesium = Trapesium("green", 0.5, 10, 7 ,5)

# Print the areas of the sha pes
print("Area of rectangle:", rect.area())
print("Area of circle:", circle.area())
print ("Area of trapesium:", trapesium.area())