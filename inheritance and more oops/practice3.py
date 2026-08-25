'''Q3. create a class "Employee" and add salary and increament proreties to it write a method salaryAfterincreament method with a @propertydecorator withe a setter which chnage values of increament based on the salary.'''
class Employee():
    salary=50000 
    increment=10
    @property  #using property we can return any thing 
    def salaryAfterincrement(self):
         return (self.salary + self.salary *(self.increment/100))

    @ salaryAfterincrement.setter #syntex-@name.setter
    def salaryAfterincrement(self, salary):
         self.increment=((salary/self.salary)-1)*100

    
a=Employee()
print(a.salaryAfterincrement)
    

         