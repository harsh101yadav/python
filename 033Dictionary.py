dic = {
    1000: "Neel Shah",
    1001: "Yash Sisodiya",
    1002: "Suraj Srinath",
    1004: "Shubham Bankar",
    1005: "Ayush Taunk",
    1006: "Harsh Yadav",
    1007: "Raj Tiwari",
    1008: "Rachit Cheda"
}

print(dic[1001])
# After python 3.7 dictionaries are ordered pairs now


info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

# print(info['name'])#This will throw a error
# print(info.get('eligible'))# This will show NONE

print(info.keys())
print(info.values())
print(info.items())

for keys in info.keys():
    print(f"The value corresponding to {keys} is {info[keys]}")