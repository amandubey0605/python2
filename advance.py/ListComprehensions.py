'''List Comprehension is an elegent way to create lists based on existing lists.
                     OR
    List comprehension is a short way to create a new list using a loop.                 

'''

'''
Syntex-numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)'''

l1=[1,2,3,4,5,6]

square=[l2**2 for l2  in l1]

print(square)














'''Normal way using a loop

Suppose we want a list of squares:

numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)

Output:

[1, 4, 9, 16, 25]
The same thing using List Comprehension ✨
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)

Output:

[1, 4, 9, 16, 25]

So this:

squares = [number ** 2 for number in numbers]

is called a list comprehension.

Simple formula 🧠
new_list = [expression for item in iterable]

Example:

[x * 2 for x in numbers]

example

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)

'''