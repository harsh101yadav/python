a = int(input("Enter number between 5 and 8 :"))

if (a<5 or a>8 ):
    raise ValueError("Number is not between 5 and 8")
else:
    print("Done!!")

