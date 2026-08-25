f=open("file3.txt","r")
# data=f.readline()  it print only one line
# print(data)      type(data) is string
data=f.readlines()       
print(data,type(data))  # it give output in a form of list and its type is list
f.close()

#    OR
f=open("file3.txt","r")
line1=f.readline()
# print(line1,type(line1))

# line2=f.readline()
# print(line2,type(line2))

# line3=f.readline()
# print(line3,type(line3))
  
# line4=f.readline()
# print(line4,type(line4))
while(line1!=""):
    print(line1)
    line1 = f.readline()
f.close()
