class Person:#class
    name = "Harsh"
    occupation = "Robotics Engineer"#attribotes
    networth = 20

    def info(self):#method
        print(f"{self.name} is a {self.occupation}")

a= Person()#object
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
