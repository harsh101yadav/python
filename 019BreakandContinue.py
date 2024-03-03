for i in range(1,12,1):
    if(i==11):
        break
    elif(i==5):
        print("continue was executed")
        continue
    print("5 X",i, "=",i*5 )
    
print("Out of loop")