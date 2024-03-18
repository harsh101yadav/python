from typing import Any


class Employee:
    def __init__(self,name,salary_increment) -> None:
        self.name = name
        self.salary_increment = salary_increment

    def __len__(self):
        i=0 
        for c in self.name:
            i=i+1
        return i
    
    def __str__(self):
        return f"The name of the Employee is {self.name} str"
    
    def __repr__(self):
        return f"The name of the Employee is {self.name} repr"
    
    def __call__(self):
        return self.salary_increment + 0.1*self.salary_increment