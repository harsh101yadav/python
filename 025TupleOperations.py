countries = ("Spain", "Italy","India","England", "Germany")
print(id(countries))
temp = list(countries)
temp.append("Russia")  #add items
temp.pop(3)#remove items
temp[2] = "Finland" # change item
countries = tuple(temp)
print(countries)
print(id(countries))# adress of countries
  


countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

#count
tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)


# index method only the first
res = tuple1.index(3)
print(res)# it will throw a value error if there is no value in the tuple
# We can also slice the tuple and then search for the value
res = tuple1.index(3,4,8)#find 3 between index 4 & 8

res = len(tuple1)
print(res)