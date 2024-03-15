class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id =id
    def show_Details(self):
        print(f"Employee no. {self.id} is {self.name}")

class Programmer(Employee):# programmer inherited the attributes of employee
    def show_language(self):
        print("The default language is python")


e1 = Employee("Harsh",100)
e1.show_Details()

e2 = Programmer("Shubham",123)
e2.show_Details()
e2.show_language()