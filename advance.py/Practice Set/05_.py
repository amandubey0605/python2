'''
Store the multiplication tables generated in problem 3 in a file name
Tables.txt. 
'''
n=int(input("Enter the number: "))

table=[n*i for i in range(1,11,1)]

with open("Tables1.txt","a+") as f:
    f.write(f"Table of {n}: {str(table)} + \n" )







