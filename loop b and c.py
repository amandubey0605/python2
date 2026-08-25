# this break statemanets use to stop exicutions immediatlly from where iteration breaks and exicute before iteration.
for i in range(1,5,1):
    # print(i)
    if i==3:
        break
    print(i)
print("loop ends here")

#  or continue(it skips iteration(i=1,i=2 etc..)and continues the exicution)
for i in range(6,11,1):
    
    if i==7:
        continue
    print(i)     
print("loop end here")  

#  pass statement (it instruct nothing to do) (without it program will throw an error )
for i in range(10):
    pass