'''
A list contains the multiplication table of  7.Write a program to convert it to vertical
string of same numbers.

'''

table =[str(7*i) for i in range(1,11)]

s="\n".join(table) #join want a list of string only

print(s)

#Q6.WAP to filter a list of a numbers which are divisible by 5.
l=[10,20,30,40,50,99]
# def divisible(n):
#     if n%5==0:
#         return True
#     return False
# a=list(filter(divisible,l))
# print(a)
#  OR
result=list(filter(lambda x:x%5==0,l))
print(result)

#Q7.WAP to find the mximum of the numbers in a list using the reduce function.
from functools import reduce
numbers=[20,30,45,67,89,56]
# def maximum(n,m):

#     if n>m:
#         return n
#     else:
#         return m
# s=reduce(maximum,numbers)
# print(s)
# OR
r=reduce(lambda x,y:x if x>y else y,numbers)
print(r)

'''Normal function	               Lambda function
Uses def	                          Uses lambda
Multiple statements allowed	          Single expression
Good for reusable complex logic	      Good for short operations

Both perform exactly the same operation.'''