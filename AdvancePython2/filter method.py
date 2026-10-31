# filter() selects only those elements that satisfy a condition.
#syntax-list(filter(function)) //the function can be lambda function
#Example: Find only even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)

#       OR
l=[1,2,3,4,5,6,7,8]
def even(n):
    if(n%2==0):
        return True
    return False

onlyEven=filter(even,l)
print(list(onlyEven))
'''
How does it work?
- x % 2 == 0 checks whether a number is even.
- filter() checks every number.
- If the condition is True, it keeps that number.
- If False, it removes that number from the result.
'''