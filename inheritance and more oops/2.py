#multiple inheritance.......
class Employee:      #parent class 
    company="ITC"
    salary=400000
    def show(self):
        print(f'The name of the company is {self.company} and salary is {self.salary}')

class coder():  #parents
    language="python"
    def printLanguage(self):
        print(f'out of all the language here is your language : {self.language}')

class Programmer(Employee,coder):    #base class or derived class
    company="ITC Infotech"
    def showLanguage(self):
        print(f'The company name is {self.company} and  good with {self.language} language')

a=Employee()
b=Programmer()
a.show()
b.printLanguage()
b.showLanguage()



print(a.company, b.company)

'''Method Overriding = Child class provides its own version of a method that already exists in the parent class.'''
                