#You have a list of numbers, and you want to multiply every number by 2.
numbers = [1, 2, 3, 4, 5]

result = []

for num in numbers:
    result.append(num * 2)

print(result)

#2
from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, numbers)

print(result)

#3
word = "madam"

print(word[::-1])