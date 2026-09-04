'''
The 'enumerate' function adds counter to an iterable and return it.
                          OR
enumerate() is a Python built-in function that helps you get both the position (index)
and the value while looping through something like a list.
'''

List=[3,4,5,6,33]
#index = 0    (without enumerate)
#for item in List:
#     print(f'The item number at index {index} is {item}')  
#     index +=1

for index,item in enumerate(List):
    print (f"The item number at index {index} is {item}")
   # print(index,item)












'''Without enumerate()
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

Output:

apple
banana
mango

Here, you only get the fruit, not its position.

With enumerate() ⭐
fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

Output:

0 apple
1 banana
2 mango

So:

index → position number
fruit → actual value'''