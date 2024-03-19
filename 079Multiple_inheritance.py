class Employee():
    def __init__(self,name) -> None:
        self.name = name

class Dancer:
    def __init__(self,dance) -> None:
        self.dance =dance
    def show(self):
        print(f"The name is {self.name}")

class DancerEmployee(Dancer,Employee):
    def __init__(self, dance,name):
        self.dance = dance
        self.name = name
    def show(self):
        print(f"The dance is {self.dance}")

o = DancerEmployee("Kathak","Mani")
print(o.name)
print(o.dance)
o.show()
print(DancerEmployee.mro())#Method resolution order
