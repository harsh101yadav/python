x =int(input("Enter your number: "))

match x:
    case 0:
        print("Number is zero")
    case 4:
        print("Number is four")
    case _ if(x!=80):
        print(x,"Number is not 80")
    case _ if(x !=90):
        print(x,"Number is not 90")
    case _:
        print(x)
