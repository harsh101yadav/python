l = [1,2,3,55,1,6,4,1]
# adding element at the end ->(append)
print(l)
l.append(7)
print(l)

#sorting a list
l.sort()
print(l)
#decreasing order
l.sort(reverse=True)
print(l)

#reverses the list
l.reverse()
print(l)


#returns only the first occurance of the list item 
c=l.index(1)
print(c)


print(l.count(1))
print(l)


#copy happens with reference
m=l
m[0]=0
print(m)
print(l)# happens due to copy via reference

#rather 
m = l.copy()
m[0]=5
print(m)
print(l)# happens due to copy via reference



#insert
l.insert(1,899)
print(l)


#extend
n= [900,55,513]
#l.extend(n)
print(l)

#how to make a list without changing the original list
k= l+n
print(k)
print(l)
