#Python does not have the concepts of public,private and protected but we can work around it as follows
class Employee:
    def __init__(self,name):
        #self.name = name #All the atributes in python are public
        self.__name = name #to help it protect form being orewited __ is used
a = Employee("Harsh")
# print(a.name)
#print(a.__name)#Throws attribute error we cannot access it
print(a._Employee__name)#but we can still access it using name mangling
#__mangled_attribute is private and its name is "mangled" to _MyClass__mangled_attribute
print(a.__dir__())


class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())