s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1.union(s2))
print(s1,s2)

s3 = s1.intersection(s2)
print(s3)

s1.intersection_update(s2)
print(s1)


s1.update(s2)
print(s1,s2)


#symmetric difference
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)


#prints only items that are only present in the original set and not in both the sets
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)

#disjoint set
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

#superset
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Berlin", "Madrid","Tokyo"}
print(cities.issuperset(cities3))
print(cities3.issubset(cities))

#add
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

#add multiple values
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

#remove (It will throw an error if item bieng removed is not present in the code)
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

#Discard (No error is thrown)
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.discard("Tokyo")
print(cities)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

#deleting a whole string
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
#del cities()        
#print(cities)# Output is a name error

#clear will only delete the elements of the set resulting into a empty set
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(type(cities))



