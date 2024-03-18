def greet(fx):
    def mfx(*args,**kwargs):
        # *args taking arguments as tuple 
        #*kwargs taking arguments as dictionaries
        print("good morning")
        fx(*args,**kwargs) # Don't forget this line or the main fun won't run 
        print("Thank you for using this function")
    return mfx

def add(a,b):
    print(a+b)

@greet
def hello():
    print("Hello world")

# Better way greet(hello)()
hello()
greet(add)(1,2)
