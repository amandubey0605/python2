'''
Q11. Calculate the sum of all numbers
numbers = [10, 20, 30, 40, 50]
# Expected output:150
'''
from functools import reduce

numbers=[10,20,30,40,50]

result=reduce(lambda x,y:x+y,numbers)

print(result)

#Q12. Calculate the product of all numbers

numbers = [2, 3, 4, 5]# Expected output:120

def mult(a,b):
    return a*b
print(reduce(mult,numbers))

#Q13.Find the maximum number

number = [12, 45, 23, 89, 34, 67] # Expected output:89

r=reduce(lambda x,y:x if x>y else y,number)
print(r)

#Q14.Join all words into one sentence
words = ["Python", "is", "very", "powerful"]# Expected output:Python is very powerful

s=reduce(lambda x, y: x + " " + y,words)
print(s)

'''Q15. Sum of squares using map and reduce
numbers = [1, 2, 3, 4, 5]# Expected output:55



For Q15:
- First use map() to square every number.
- Then use reduce() to add all squared numbers.'''
# from functools import reduce
num=[1,2,3,4,5,6]

square=list(map(lambda x:x**2,num))

sum=reduce(lambda x,y:x+y,square )

print(sum)






