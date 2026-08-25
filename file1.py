f=open("file.txt","r")   # or f=open("file.txt") because open function is by defualt  readable mode.
data=f.read()
print(data )
f.close()