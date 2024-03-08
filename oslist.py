import os 

if(not os.path.exists("data")):
    os.mkdir("data")

folders = os.listdir("data")
print(os.getcwd())

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))