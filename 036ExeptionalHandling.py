# a = input("Enter the number: ")
# print(f"The Multiplication table of {a} = ")

# for i in range(1,11):
#     print(f" {a} X {i} = {int(a)*i}")

# What if someone enters a string then we need try and exception
    
a = input("Enter the number: ")
print(f"The Multiplication table of {a} = ")
try:
    for i in range(1,11):
        print(f" {a} X {i} = {int(a)*i}")
except Exception as e:
    print(e)

print("Some imp lines of code \nEnd of program")


try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")