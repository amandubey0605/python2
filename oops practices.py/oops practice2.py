#Write a class "calculator" capable of finding square, cube and square root of a number
class Calculator:
    # n=int(input("enter the number: "))
    def __init__(self,n):
       self.n=n

    def square (self):
        print(f'square is {self.n*self.n}') 
    def cube (self):
        print(f'cube is {self.n*self.n*self.n}') 
    def squareRoot (self):
        print(f'square root is {self.n**0.5}') 
n=int(input("Enter the number: "))
a=Calculator(n)
a.square()
a.cube()
a.squareRoot()

'''Your code is **correct** ✅. You have successfully created a `Calculator` class that finds the **square, cube, and square root** of a number.

Let's understand it simply:

```python
class Calculator:
```

This creates a class named `Calculator`.

```python
def __init__(self, n):
    self.n = n
```

This is the **constructor**. When you create an object, it stores the number inside `self.n`.

```python
a = Calculator(n)
```

Here, `a` is an **object** of the `Calculator` class, and the value of `n` is passed to the constructor.

### Your methods:

```python
def square(self):
    print(f'square is {self.n*self.n}')
```

Finds the square:

**5 × 5 = 25**

```python
def cube(self):
    print(f'cube is {self.n*self.n*self.n}')
```

Finds the cube:

**5 × 5 × 5 = 125**

```python
def squareRoot(self):
    print(f'square root is {self.n**0.5}')
```

Finds the square root using:

**n⁰·⁵ = √n**

For example, if you enter `25`, output will be approximately:

```text
Enter the number: 25
square is 625
cube is 15625
square root is 5.0
```

### The important concept you learned here:

**Class → Object → Constructor → Methods**

```text
Calculator (Class)
       ↓
   a (Object)
       ↓
__init__(n) stores number
       ↓
square() → finds square
cube() → finds cube
squareRoot() → finds square root
```

Great job! 👍 This is a good example of **Object-Oriented Programming (OOP)** in Python.
'''