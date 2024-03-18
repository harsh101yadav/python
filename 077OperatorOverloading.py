class Vector:
    def __init__(self,x,y,z) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self) -> str:
        return f"{self.x}i + {self.y}j + {self.z}k"

    def __add__(self,x):
        return (self.x +x.x, self.y+x.y , self.z+x.z)

v1 =Vector(1,2,3)
print(v1)
v2 = Vector(3,2,1)
print(v2)
print(v1+v2)