#Either try or except is executed finally will always be executed
a = [1,3,5,67]
try:
    i = int(input("Enter the index: "))
    print(a[i])
except:
    print("Chichi error")
finally:
    print("I am always executed")
#print("I am always executed") #This type of statement will also work but we will not use it as it will fail in function calling as shown below
    
def ind():
    a = [1,3,5,67]
    try:
        i = int(input("Enter the index: "))
        print(a[i])
        return 1
    except:
        print("Chichi error")
        return 0
    finally:
        print("I am always executed")

x = ind()
print(x)