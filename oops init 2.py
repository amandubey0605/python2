class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Aman", 20)
student2 = Student("Rahul", 21)

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)

# Of course, Aman 😊 Let's understand **`self` and `__init__()` together** in the simplest way.

## 🧑‍🎓 Real-life example: Student

'''Imagine we have a **Student form**. Every student has a **name** and **age**.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Aman", 20)
student2 = Student("Rahul", 21)

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)'''


### Output:

'''```text
Aman
20
Rahul
21
```

Now let's understand the two important things.

---

### 1️⃣ What is `__init__()`?

```python
def __init__(self, name, age):
```

`__init__()` runs **automatically when you create an object**.

When you write:

```python
student1 = Student("Aman", 20)
```

Python automatically runs:

```python
__init__("Aman", 20)
```

Its job is to **set the initial information** of the student.

---

### 2️⃣ What is `self`?

`self` means **"this particular object"**.

For example:

```python
student1 = Student("Aman", 20)
```

Here, `self` refers to **`student1`**.

So:

```python
self.name = name
```

means:

> Store the name `"Aman"` inside **student1**.

And:

```python
self.age = age
```

means:

> Store the age `20` inside **student1**.

Then we create another student:

```python
student2 = Student("Rahul", 21)
```

Now `self` refers to **`student2`**.

So:

```python
self.name = name
```

means:

> Store `"Rahul"` inside **student2**.

---

### 🧠 Super Simple Memory Trick

Think of a **student form**:

```text
__init__() → Fill the form when creating a student
self       → Which student's form?
```

So:

```python
self.name = name
```

means:

> **This student's name = the name given to me**

### ⭐ Remember this:

> **`__init__()` sets the data.**
> **`self` tells Python which object's data to set.**

For now, if you remember just these two lines, you're doing great:

```python
def __init__(self, name):
    self.name = name
```

**`name`** → the value coming in
**`self.name`** → the value stored inside that particular object.'''
