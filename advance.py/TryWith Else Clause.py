'''
Sometimes we want to run a piece of code when try was successful.

tyr(catch hota hai C, C++ me) and python me try except hota hai

'''
try:  #first it try if it run or not (sahi hoga to print hoga nhi to exception print hoga)
    a=int(input("enter the number: "))
    print(a)
 

except Exception as e:
    print(e)  

else:    #try agar successful hoga tabhi else run hoga.
    print("I am inside else") #it is the piece of code
