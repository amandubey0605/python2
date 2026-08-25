# WAP to rename a file to "renamed_by_python.txt". using python

# with open("old.txt","r") as f:
#     content=f.read()


# with open("renamed_by_python.txt","w") as f:
#     f.write(content)

# os module he os module is a built-in Python module that provides functions for interacting with the operating system, such as working with files and directories.
import os
os.rename("old1.txt","renamed_by_python.txt")