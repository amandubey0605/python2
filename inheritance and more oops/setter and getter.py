'''1. Getter — "Get the value"

A getter is used to read/access a value.

With @property, the method acts as a getter.

class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

Now:

e = Employee(50000)

print(e.salary)

Output:

50000

Here:

@property
def salary(self):
    return self._salary

is the getter.

👉 It gets/returns the salary.

Think:

Getter = I want to GET/read the value. 📖

2. Setter — "Set/change the value"

A setter is used when we want to change/update a value.

We use:

@salary.setter

Example:

class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary

Now:

e = Employee(50000)

print(e.salary)  # Getter

e.salary = 60000  # Setter

print(e.salary)  # Getter

Output:

50000
60000
What happened?

When we write:

print(e.salary)

Python calls the getter:

@property
def salary(self):
    return self._salary

When we write:

e.salary = 60000

Python calls the setter:

@salary.setter
def salary(self, new_salary):
    self._salary = new_salary

So:

             Employee
                 │
        ┌────────┴────────┐
        │                 │
     Getter             Setter
     READ                CHANGE
        │                 │
   e.salary         e.salary = 60000
        │                 │
   Gets value        Sets new value
🧠 The easiest way to remember:

Getter → GET/READ the value
Setter → SET/CHANGE the value'''