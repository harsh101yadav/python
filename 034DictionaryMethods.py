dic1 = {
    1:90,2:46,3:68,4:65
}
dic2 = {
    5:56,6:99
}

print(dic1)
print(dic2)

dic1.update(dic2)

print(dic1)
print(dic2)

#dic1.clear()
print(dic1)


emp = {}
print(emp)

dic1.pop(3)
print(dic1)

#pop item deletes the last element of the dictionary
dic1.popitem()
print(dic1)

#similar to sets del methods it will throw an error
# del(dic1)
print(dic1)

del(dic1[2])
print(dic1)
