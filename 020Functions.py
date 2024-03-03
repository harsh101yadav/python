def GM(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    elif(a==b):
        print("Number are equal")
    else:
        print("Secomnd number is greater")


def isLesser(a,b):
    pass

a =int(input("Enter the number a : "))

b = int(input("Enter the number b : "))

GM(a,b)