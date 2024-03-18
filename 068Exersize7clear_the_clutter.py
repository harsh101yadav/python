"""
Write a program to clear the clutter inside a folder on your computer. 
You should use os module to rename all the png images from 1.png all 
the way till n.png where n is the number of png files in that folder. 
Do the same for other file formats. For example:

sfdsf.png --> 1.png
vfsf.png --> 2.png
this.png --> 3.png

design.png --> 4.png
name.png --> 5.png
"""

import os
# print(os.__dict__)
# print(help(os))

def Clear_folder(folder_path):
    files = os.listdir(folder_path)
    print(files)
    new_files =[]
    for file in files:
        if file.endswith(".png"):
            new_files.append(file)

    print(new_files)
    for i,file in enumerate(new_files):
        new_files_names = f"{i+1}.png"
        os.chdir("D:\Study Material\Subjects\Python\Clutter")
        os.rename(file, new_files_names)
    


folder_path = "D:\Study Material\Subjects\Python\Clutter"

Clear_folder(folder_path)