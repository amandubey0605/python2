# inheritance is a way of creating new class from an existing class.
#type of inheritance 1.single inheritance 2. multiple inheritance 3. multilevel inheritance
  #single inheritance-- single inharitance occurs when child class inherits only a single parent class
  #multiple inharitance occurs when the child class inherits from more than one parent classes.
  #multilevel inhartance-  when a child becomes a parent for another child class

#1. Parent Class

'''parent class is the class whose properties and methods are inherited (given) to another class.

 2. Child Class

 A child class is the class that inherits properties and methods from the parent class.'''

class Employee:      #parent class 
    company="ITC"
    def show(self):
        print(f'The name of the Employee is {self.name} and salary is {self.salary}')

      #we can use the method and attributes of "employee" in "programmer" object.
      #also,we can overwrite or add new attributes and methods in"programmer" class

class Programmer(Employee):  #base class or derived class
    company="ITC Infotech"
    def showLanguage(self):
        print(f'The name is {self.name} and he is good with {self.language} language')

a=Employee()
b=Programmer()
a.show()

print(a.company, b.company)
                