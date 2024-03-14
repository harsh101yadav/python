import random
l = [#snake, water, gun => computer
    [0,1,-1],#snake
    [-1,0,1],#water
    [1,-1,0],#gun
    #^Player^ 1= win, 0=draw & -1= loss
]


def calling():
    x = input("What will you choose:(Snake,Water,gun or Quit): ")
    x = x.lower()
    return x

def random_generate():
    x = random.randint(0,2)
    return x

def check(x,y):
    a = l[x][y]
    if(y==0):
        print("The bot chooses Snake")
    elif(y==1):
        print("the bot chooses Water")
    else:
        print("The bot chosses Gun")

        
    if(a == 0):
        print("Match was a draw")
    elif(a == 1):
        print("Wow you actually won")
    elif(a ==-1):
        print("Oh no you lost!")




print("Welcome to are you better than my code: ")
x= calling()

while True:
    if(x == "snake"):
        x = 0
        y = random_generate()
        check(x,y)

    elif(x == "water"):
        x= 1
        y = random_generate()
        check(x,y)

    elif(x == "gun"):
        x=2
        y = random_generate()
        check(x,y)

    elif(x =="quit"):
        print("bye bye. Hope to see you agian.")
        break
    else:
        print("This is not apart of the game.\nEnter a correct input")

    print("Let's try again")
    x = calling()