class MyClass:
    def __init__(self, value):
        self._value = value
    
    def show(self):
        print(f"the value is {self._value}")

    @property # @property used to create getters
    def ten_value(self):
        return 10*self._value

    @ten_value.setter  # @method nane.setter used to create setters
    def ten_value(self,new_value):
        self._value = new_value/10

obj =MyClass(10)
#obj.ten_value() does not work
#obj.ten_value =67 -> Attribute error if setter not set
obj.ten_value = 67
print(obj.ten_value)
obj.show()