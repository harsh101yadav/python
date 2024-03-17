# class ParentClass:
#     def parent_method(self):
#         print("This is a parent class")

# class ChildClass(ParentClass):
#     def parent_method(self):
#         print("Harsh")
#         super().parent_method()

#     def child_method(self):
#         print("This is a child class")
    
#         super().parent_method()

# child_object = ChildClass()
# child_object.child_method()
# child_object.parent_method()

class Employee:
    def __init__(self,name,id) -> None:
        self.name = name 
        self.id = id
class Programmer(Employee):
    def __init__(self,name,id,lang) -> None:
        super().__init__(name,id)
        self.lang = lang

e1 = Employee("yash",123)
p1 = Programmer("Harsh",321,"Python")
print(p1.name)