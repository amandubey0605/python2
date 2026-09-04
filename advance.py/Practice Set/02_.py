'''
Write a program to print third (index value 2),fifth (index value 4)and seventh(index value 6) element from a list using enumerated
function? if l1=[1,2,3,4,5,6,7]
'''
l1=[0,1,2,3,4,5,6,7]  #

for index,item in enumerate(l1):

    if index==3 or index==5 or index==7: #agar index se krna hota to 3 ,5 ,7 likhte 
        print(item)
        
print("ThankYou!")

        