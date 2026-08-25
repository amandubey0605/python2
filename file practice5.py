#A file contains a negative words in a list multiple times. you need to write a program which replace the word with ##### by updating the same file.

words=["donkey", "foolish","bad","fool"]

with open("filep5.txt","r") as f:
    content=f.read()

for word in words:
    content=content.replace(word,"#####")

with open("filep5.txt","w") as f:
    f.write(content)   

