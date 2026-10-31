'''
map- Map applies a function to all the items in an input_list
syntax-map(function,input_list)   //the function can be lambda function

- map() applies this operation to every number.
'''
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))

print(result)

'''
How does it work?
- lambda x: x * 2 means take a number and multiply it by 2.
- map() applies this operation to every number.
- list() converts the result into a list.
'''