class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary =salary

    @classmethod#alternative constructor
    def fromstring(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])

e1 = Employee("harsh",10)
print(e1.name)
print(e1.salary)

string = "Viki-20"
e2 =Employee.fromstring(string)
print(e2.name)
print(e2.salary)