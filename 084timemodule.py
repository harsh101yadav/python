import time

def forloop():
    count =0 
    for i in range (5000):
        count= count+ 1
def whileloop():
    i=0
    count = 0
    while(i<5000):
        count =count +1
        i = i+1

init = time.time()
forloop()
t1 = time.time() -init
init = time.time()
whileloop()
t2 = time.time() -init
print(f"Time taken for for loop is {t1} sec \n Time taken for while loop is {t2} sec")


print(4)
time.sleep(3)
print("This is printed after 3 seconds")
 
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time) 