a = "!!!!!! Harsh!!!!!!!!!!! Harsh!!!"
# strings are immutable
print(a.upper())
# print(a.lower())
print(a)

print(a.rstrip("!"))

#replace all
print(a.replace("Harsh","Rashmi"))


#Spliting a string
print(a.split(" "))

#capatalizing the firdt letter and making all the other charaters small case
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

str1= "introduction tO jS"
print(len(str1))
print(len(str1.center(50)))


print(a.count("Harsh"))

print(a.endswith("!!!"))


print(a.endswith("on",4,11))


#find= finds the first occurance and returns index
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))


#index method => similar to find()
# in case on find if no occurances it returns -1.
# whereas in index it throws an error
print(str1.find("issh"))
# print(str1.index("issh"))


#isalnum -> tells if a string only has alphabets and numbers
str1 = "WelcomeToTheConsole123"
print(str1.isalnum())


#isalpha
print(str1.isalpha())


#islower
b= "harsh and rashmi sitting in a tree"
print(b.islower())

#isprintable -> works if only characters are printable
str1= "Hello darkness\n"
print(str1)
print(str1.isprintable())

#isspace
str1= "          " #using spacebar
print(str1.isspace())

str2 = "            " #using tab
print(str2.isspace())


str1 = "World Health Organization"
print(str1.istitle())


#isUpper -> same as islower()
str1 = "HELLO"
print()

str1 = "HELLO"
print(str1.startswith("H"))  


str1 = "HELLO"
print(str1.swapcase())  

str1 = "He's name is Dan. He is an honest man."
print(str1.title())