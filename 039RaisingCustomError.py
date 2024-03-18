# a = int(input("Enter number between 5 and 8 :"))

# if (a<5 or a>8 ):
#     raise ValueError("Number is not between 5 and 8")
# else:
#     print("Done!!")

try:
    a = int(input("Enter number between "))
    if (a<5 or a>8 ):
        raise ValueError("Number is not between 5 and 8")
    else:
        print("Done!!")
except ValueError:
    if (a == "quit"):
        print("Okay let's quit")
    else:
        raise ValueError("Enter a Number")