'''Operator overloading means giving a special meaning to an operator (+, -, *, /, etc.) when it is used with objects of a class.
Operator overloading means defining how an operator behaves when it is used with objects of our class.
In simple words:

We tell Python what an operator should do with our class objects.

Example
class Number:
    def __init__(self, n):
        self.n = n


    def __add__(self, other):
        return self.n + other.n




a = Number(10)
b = Number(20)


print(a + b)

Output:

30
Why?

When Python sees:

a + b

it calls:

a.__add__(b)

So __add__() tells Python how to perform + between two Number objects.

⭐ Remember these
Operator	Special method
+	__add__()
-	__sub__()
*	__mul__()
/	__truediv__()
.   __str__()  -(a string method used to set what gets displayed when calling a string)
.   __ien__() -(used to set what get displayed upon calling.(len(obj)))


'''
class Number:
    def __init__(self,n):
        self.n=n

    def __add__(self,other):
        return self.n + other.n

a=Number(10)
b=Number(20)

print(a+b)

'''When Python sees:

a + b

it calls:

a.__add__(b)

So inside:

def __add__(self, other):
self → a → 10
other → b → 20

Then:

return self.n + other.n

becomes:

10 + 20
= 30
⭐ Your code vs my example

You used:

self.n

instead of:

self.value

That's completely fine. The variable name can be anything you choose.

🚀 Challenge 3 — Subtraction

Now you write the code yourself.

Create a Number class that supports:

a - b

where:

a = 50
b = 20

Expected output:

30

💡 Hint: You need:

__sub__

Don't copy the previous code blindly. Try writing it yourself.

Your comeback has officially started. 🐍🔥'''