'''
Reduce() combines all elements into a single result by repeatedly applying a function.

It is available through the functools module.

syntex- from functools import reduce
val=reduce(function,list)  //the function can be lambda function

Q1-what is functools module

functools is a built-in Python module that provides useful tools for working with functions.

In simple words:

It contains functions that help us work with, modify, and combine other functions.


2. Some useful tools inside functools
Function	Purpose
reduce()	Combines elements into one result
lru_cache()	Caches function results to avoid repeated calculations
partial()	Creates a new function with some arguments already filled
wraps()	Preserves function information when using decorators
'''
from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, numbers)

print(result)

#   OR

l=[1,2,3,4,5,6,7,8]

def sum(a,b):
    return a+b

print(reduce(sum,l))


'''
How does it work?

Let's understand step by step:
Step	Calculation   Result
1	      1 + 2	       3
2	      3 + 3	       6
3	      6 + 4	      10
4	      10 + 5	  15

Final answer = 15.


4. Difference between map, filter and reduce
M

map()

Changes every element.

[1, 2, 3] → [2, 4, 6]



F

filter()

Selects elements based on a condition.

[1, 2, 3, 4] → [2, 4]



R

reduce()

Combines elements into one result.

[1, 2, 3, 4] → 10



Remember this simple trick:
- Map = Modify
- Filter = Select
- Reduce = Combine
'''


