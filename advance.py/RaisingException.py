'''We can raise custom exceptions using the 'raise'keyword in python'''
a=int(input("enter the number: "))
b=int(input("enter the number: "))

if(b==0):
    raise ZeroDivisionError("our program is not meant to divide numbers by zero")
    '''suppose we are making module in python that people import it and you not want 
    anyone do mistake in this so we immidiatly stop them or crash their program we
     know that our program should not crash but sometime it have to crash because 
    if our developer doing a mistake and he know about the mistake what he done when his
    program will crash and the developer fixed it'''
else:
    print(f'The Division a/b is {a/b}')


