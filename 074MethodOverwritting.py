class Shape:
    def __init__(self,x,y) -> None:
        self.x =x 
        self.y = y
    
    def area(self):
        return self.x*self.y
    
class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__(radius, radius)

    def area(self):
        return 3.14*super().area()
# rec = Shape(2,3)
# print(rec.area())

cir = Circle(5)
print(cir.area())
    