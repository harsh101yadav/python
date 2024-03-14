class Person:
    def __init__(self,name,occ):#dundors method
        print("I am a person")
        self.name = name
        self.occ = occ
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Harsh","Robotics Engineer")
b= Person("Suraj","Data Science Engineer")

a.info()
b.info()