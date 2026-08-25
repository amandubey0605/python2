# self reffer to the instance of the class (object).it automatically passed with a function call from an object.
#When you create a class, self is used to access the data and functions belonging to that object.
class Employee:
    name="aman"
    language="py"
    salary="300000"
    def getInfo(self):  #def is function and getInfo is a method
        print(f"the language is: {self.language}  the salary is: {self.salary}")

    def greet(self):
        print(f"good morning {self.name}")

aman=Employee()       #object
aman.name="aman"    #object or instance attribute

aman.getInfo()
aman.greet()
   #if we call object it convert into Employee.getInfo(aman) here aman given and if we not give parameter or argument in def function(self) it give error
#  or 
#Employee.getInfo(aman)