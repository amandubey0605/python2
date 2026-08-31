'''
There are many built-in exceptions which are raised in python when something
goes wrong.

Execption in python can be handled using a try statement . the code that handles the execption
is written in except clause
'''
'''
try:
    #code which might throw exception

except Exception as e:
    print(e)    
    
(2)
try:
    #code
except ZeroDivisionError:
    #code
except TypeError:
    #code
except:
    #code        #all other exceptions are handled here. '''

try:  #first it try if it run or not (sahi hoga to print hoga nhi to exception print hoga)
    a=int(input("enter the number: "))
    print(a)
except ValueError as err:
    print("it print value error")
    print(err)

except Exception as e:
    print(e)  




'''the e is not special. It is simply a variable name.

What does it do?

When an error occurs, Python stores the exception object in e.

Example:

try:
    num = 10 / 0
except Exception as e:
    print(e)

Output:

division by zero

Here, e contains information about the error.

Why do people usually use e?

Because e means Exception/Error by convention.

But you can use any valid variable name:

except Exception as error:
    print(error)

or:

except Exception as err:
    print(err)

All work similarly.'''     