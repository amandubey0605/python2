# WAP to find out whether a file is identical(they look like same) and matches the content of another file
with open("this.txt","r") as f:
    content=f.read()

with open("this_copy.txt","r") as f:
    content2=f.read()

if content2 == content:
    print("the files are identical ")

else:
    print("the files are not identical")


