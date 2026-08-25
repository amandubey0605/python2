n=int(input("enter the number here: "))
for i in range(1,11,1):
    # print(f'{n*i}')   or
    print(f'{n} x {i}= {n * i}')

# Q2. WAP to greet all the person names stored in a list'l' and which starts with A
# l=  ["Aman","Ankit","Aparna","shinuu","rahul"]   
l=  ["Aman","Ankit","Aparna","shinuu","rahul"]   

for names in l:
    if(names.startswith("A")):
        print(f'hello: {names}')
    # else:
    #     print("names not start with A: ",names) 
print("code ends here")           



  