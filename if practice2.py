# WAP to find greatest number among 4 number entered by user
a=int(input("enter the first no: "))
b=int(input("enter the second no: "))
c=int(input("enter the third no: "))
d=int(input("enter the fourth no: "))

if(a>b and a>c and a>d ):
    print("greater no: ",a)
elif(b>c and b>d):
    print("greater no: ",b)
elif(c>d):
    print("grater no: ",c)
else:
    print("grater no: ",d)  

print("code ended")
     
    
