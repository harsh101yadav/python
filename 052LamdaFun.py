# lambda functions are used mainly to pass function as an argument
# def double(x):
#     return x*2
def appl(fx, value):
    return 6 + fx(value)

double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda x,y,z: (x+y+z)/3
# appl(cube,2)
#rather we can use
appl(lambda x:x*x*x , 2)# this lamda fun does not have a name

print(double(5))
print(cube(5))
print(avg(5,15,10))