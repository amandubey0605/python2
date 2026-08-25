# WAP using functions to find greatest of three numbers.
def greater(a,b,c):
    if(a>b and a>c):
        print("a is greater",a)
        #return a
    elif(b>c):
        print("b is greater",b)
        #return b
    else:
        print("c is greater",c)
       # return c
       
greater(5,4,3)

#  OR
def greatest1(r,t,y):
    if(r>t and r>y):
        return r
    elif(t>y and t>y):
        return t
    else:
        return y
result=greatest1(5,15,18)    
print(f"greatest number among three is: {result}")    
  
     