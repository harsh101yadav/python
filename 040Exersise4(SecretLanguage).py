import random
import string

ran = string.ascii_letters

x = input("Enter what you want to do")
while True:
    # if x == "code" or "Code" or "decode" or "Decode":
    if x.lower() in ['code', 'decode']:
        break
    else:
        x = input("Enter code or decode")

x= x.lower()

if(x== "code"):
    string1 = input("Enter the string you want to code")
    words = string1.split()
    for word in words:
        if len(word) <= 3:
            word = word[::-1]
        else:
            first = word[0]
            word =  word[1:]
            word = word + first
            k=""
            for i in range(3):
                random_letters= random.choices(ran)
                k = k + random_letters[0]
            word = k+word+k
        print(word,end=" ")

elif(x=="decode"):
    string1 = input("Enter the string you want to code")
    words = string1.split()
    for word in words:
        if len(word) <= 3:
            word = word[::-1]
        else:
            word = word[3:-3]
            last = word[-1]
            word = word[:-1]
            word = last + word
        print(word,end=" ")
