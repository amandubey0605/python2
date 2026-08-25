'''override the __len__() method on vactor of problem 6 to display the dimension of all the  vector'''
#firstly Override means = change/replace the normal behavior of a method for your own class.
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x}i +{self.y}j + {self.z}k" 

    def __len__(self):  #function
        return len(self.x)+len(self.y)+len(self.z)
v = Vector("aman", "kumar", "dubey")

print(len(v))
 #   OR
class Vector2:
    def __init__(self,l):
        self.l=l

    def __len__(self):
       return len(self.l)

v1=Vector2([1,2,3])
print(len(v1))         









'''1. What does "override" mean?

Override = change/replace the normal behavior of a method for your own class.

For example, Python already has a built-in len() function:

name = "Aman"
print(len(name))

Python knows how to calculate the length of a string.

But suppose we create our own Vector class:

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

If we try:

v = Vector(7, 8, 10)
print(len(v))

Python doesn't automatically know what "length" means for our Vector.

So we override __len__() and tell Python:

"Whenever len() is used on my Vector object, use MY definition of length."

2. The important connection 🧠

Remember:

print(v)

can be controlled using:

__str__()

Similarly:

len(v)

can be controlled using:

__len__()

So:

Normal operation	Special method
print(v)	__str__()
len(v)	__len__()
v1 + v2	__add__()
v1 - v2	__sub__()
v1 * v2	__mul__()

That's operator/special-method thinking. 👍

3. Now your problem

"Override the __len__() method on'''