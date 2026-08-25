
import os
# specify the directory you wnt to list (problem 4)
directory = '/'

if os.path.exists(directory):
    print("Contents of", directory)  # here os.listdir(directory) is list of all file and directory in a specified path  

    for item in os.listdir(directory): 
        # print each file and directiory name
        print(item)
else:
    print("Directory does not exist.")