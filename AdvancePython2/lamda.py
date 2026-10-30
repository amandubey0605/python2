'''function created using an expression using "lamda" keyword.
or 
A lambda function is a small, anonymous function written in a single expression using the lambda keyword.
- lambda — creates the function.
- Parameters — the inputs.
- Expression — the calculation or value returned.

important point-
A lambda function can take zero, one, or multiple parameters.

It contains one expression, not a normal block of statements.

Its expression's result is returned automatically.

You can assign it to a variable, although a normal def function is usually clearer for reusable, complex logic.

Lambda functions are often used with map(), filter(), and sorted().

syntex-
lambda arguments:expressions
#can be used as normal function

example-
square=lambda x:x*x
square(6) #return 36
sum= lambda a,b,c:a+b+c
sum(1,2,3) #return 6

'''
#def square(n):
    #return n*n

#S=square(5)

#print(S)
#     OR

square=lambda x:x*x   # single line function

print(square(5))




