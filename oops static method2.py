''' static method (syntex- @staticmethod) some times we need a function that does not
use the self-parameter.we can define a static method'''
class Employee:
    name="aman"
    language="py"
    salary="300000"
    def getInfo(self):  #def is function and getInfo is a method
        print(f"the language is: {self.language}  the salary is: {self.salary}")

    @staticmethod  #telling it is not self parameter agar hamko object se kuch nhi chahiye
                   # na salary na lanuguage bs print krna hai 

    def greet():#greet ek function tha jisko hamlog pura "aman" object pass kr diya self
                # parameter ke help se link hamlog ko bina object diye function run krna 
                # hai to static method lagega(then call it)

        print(f"good morning {aman.name}")

aman=Employee()       #object
aman.name="aman"    #object or instance attribute

aman.getInfo()
aman.greet()