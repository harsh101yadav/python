from functools import reduce
# def cube(x):
#     return x*x*x
l = [1,2,4,6,7]
# newl = []
# for item in l:
#     newl.append(cube(item))

#MAP
#better way via map
newl = list(map(lambda x: x*x*x,l))# used map fun then made it into a list
print(newl)

#FILTER
def greater(a):
    return a>3

newnewl = list(filter(greater,l))
print(newnewl)

#REDUCE
#First we need to import the reduce function as written in line one
number = [1,2,3,4,5]

sum = reduce(lambda x,y: x+y, number)
print(sum)