class Employee:
    company_name = "Boston Dynamics"#class variable
    def __init__(self,name):
        self.name = name
        self.raise_amount =0.02#instant variable
    
    def show_name(self):
        print(f"The name of the employee is {self.name} and the raise in {self.company_name} will be {self.raise_amount}")

e1 = Employee("Harsh")
e1.show_name()# same as below line 
#Employee.show_name(e1)

e2 = Employee("Rashmi")
e2.raise_amount = 0.03
e2.company_name = "Apple"
e2.show_name()