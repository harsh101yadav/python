marks = [4,5,9,"Harsh",True,5,54,12,46,6,6.4,5]
print(marks)
print(type(marks))

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

#negative indexing
print(marks[-3])
print(marks[len(marks)-3])
print(marks[5-3])
print(marks[2])

if "Harsh" in marks:
    print("Yes")
else: 
    print("No")

#Same thing applies for string as well
if "Ha" in "Harsh":
    print("Yes")


print(marks)
print(marks[:])
print(marks[1:(len(marks)-1)])
print(marks[1:9:2])#Here 2 is the jump index

# list comprihension
lst = [ i*i for i  in  range(10)]
print(lst)

lst = [ i*i for i  in  range(10) if i%2==0]
print(lst)


names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_4 = [items for items in names if len(items)>4]
print(namesWith_4)