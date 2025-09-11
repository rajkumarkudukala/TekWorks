from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, b):
        self.length = l
        self.breadth = b
    def area(self):
        return self.length * self.breadth
    
class Circle(Shape):
    def __init__(self, r):
        self.radius = r
    def area(self):
        return 3.14*self.radius*self.radius
    
r = Rectangle(5,4)
c = Circle(5)

print(r.area())
print(c.area())