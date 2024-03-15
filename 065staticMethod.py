class Math:
    def __init__(self,n):
        self.num =n

    def add_to_num(self,n):
        self.num = self.num + n
        print(f"The sum is {self.num}")

    @staticmethod
    def add(x,y):
        return x+y
    
a = Math(5)
a.add_to_num(6)
print(a.add(3,4))
print(Math.add(3,4))
