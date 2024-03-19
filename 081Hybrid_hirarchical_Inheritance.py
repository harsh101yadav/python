#Hybrid Example
class BaseClass:
    pass

class Derived1(BaseClass):
    pass

class Derived2(BaseClass):
    pass

class Derived3(Derived1,Derived2):
    pass

#Hirarchical Inheritance
class Base():
    pass

class D1(Base):
    pass
class D2(Base):
    pass
class D3(D1):
    pass