'''Write a class complex to represent complax numbers,along with overloaded operators"+" and "*" which add and multiplies them'''
class Complex():
    def __init__(self,n,m):
        self.n=n  #number
        self.m=m   #imaginary number

    def __add__(self, other):
        return Complex( 
            self.n + other.n,
             self.m + other.m  
     ) 

    def __mul__(self, other):
        return Complex(
           self.n * other.n-self.m * other.m,
           self.n * other.m + self.m * other.n
    )
    def __str__(self):     #__str__ = tells Python what the object should look like
        return f'{self.n} + {self.m}i'   #"Show my real part + imaginary part i."

a=Complex(2,3)  # (a +bi)
b=Complex(4,5)  # (c+ di)
                #(a +bi)*(c+ di) = (ac - bd) + (ad + bc)i   
print(f'The sum is: {a+b}')

print(f'The multiplication is : {a*b}')


'''Think about your object

You created:

a = Complex(2, 3)

Python sees a as an object.

Inside a:

n = 2
m = 3

So you know that a means:

2 + 3i

But Python doesn't automatically know that you want to display it as 2 + 3i.

Without __str__

Suppose you write:

class Complex:
    def __init__(self, n, m):
        self.n = n
        self.m = m

a = Complex(2, 3)

print(a)

Python doesn't know how you want the object to be displayed.

So you get something ugly like:

<__main__.Complex object at 0x...>
Now we teach Python how to display it

You write:

def __str__(self):
    return f'{self.n} + {self.m}i'

You're basically telling Python:

"Whenever someone tries to print my Complex object, display it like this."

So:

print(a)

Python uses your __str__:

2 + 3i

That's it. That's the whole idea. 😄

Think of it like a translator

Your object:

a
↓
Complex(2, 3)

Python normally:

"How do I display this object?"

Your __str__ says:

"Display it as 2 + 3i."

So:

print(a)

➡️ 2 + 3i'''