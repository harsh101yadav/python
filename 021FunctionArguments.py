#default arguments
def average(a=6,b=4):
    print("Average of value :",(a+b)/2)

# average()
# average(5)

#Keyword argument
average(b=5,a=3)



# a is a required argument that needs to be passed in the correct order
def average(a,b=4):
    print("Average of value :",(a+b)/2)

average(a=3)


def average1(*numbers):
    print(type(numbers))
    sum =0
    for i in numbers:
        sum = sum + i
    print("Average of values :", sum/(len(numbers)))


average1(1,2,3)


#for dictonaries
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])
name(mname = "Buchanan", lname = "Barnes", fname = "James")

#return function
def average1(*numbers):
    print(type(numbers))
    sum =0
    for i in numbers:
        sum = sum + i
    return sum/(len(numbers))

c = average1(1,2,3)
print(c)