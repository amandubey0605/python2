'''
Write a list comprehension to print a list which contains a multiplication table
of a user entered number.
'''
n=int(input("Enter the number: "))

table=[n*i for i in range(1,11,1)]
print(table)





