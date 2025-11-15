import math
class Circle:
    def __init__(self,r):
        self.radius =r
    
    def Area(self):
        return (math.pi*self.radius**2)
    def Perimeter(self):
        return (2*math.pi*self.radius)
    
circle1 = Circle(10)
print("Area is:",circle1.Area())
print("Perimeter is:",circle1.Perimeter())