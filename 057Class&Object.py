class Person:
    name = "Harsh"
    occupation = "Robotics Engineer"
    networth = 20

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a= Person()
b= Person()
c= Person()

a.name = "Shubham"
a.occupation = "Data Engineer"
b.name = "Rashmi"
b.occupation = "Engineering Scholar"
# print(a.name,a.occupation)
a.info()
b.info()
c.info()
