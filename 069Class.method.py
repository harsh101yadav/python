class Employee:
    company = "Apple"
    def show(self):
        print(f"Employee named {self.name} works in {self.company}")
    
    @classmethod #Used to change class variable
    def Change_company(cls,newComppany):
        cls.company = newComppany

e1 =Employee()
e1.name = "Harsh"
e1.show()
e1.Change_company("Tesla")
e1.show()
print(Employee.company)