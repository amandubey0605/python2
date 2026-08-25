''' __init__() is a speacial method which is first run as soon as the object is created
(2). __init__() method is also known as constructor
(3).it takes self-argument and can also take further argument 
SYNTEX-- __init__(self,name):
it is dunder methods(function start with one or double underscore"_") which is automatically called.
it is used to give initial values to an object when the object is created

1.calss=blue print(like house)
2.object=actual house(house)
3.init=setting up the house when it is built  '''

class Employee:
    name="aman"
    language="py"
    salary="300000"

    def __init__(self,name,salary,language):#dunder method 
        self.name=name      #  the value writen in the boject "aman=Employee()" is assigned
        self.salary=salary   # here
        self.language=language 
        
        print("i am run automaically when object is created")

    

    def getInfo(self):  #def is function and getInfo is a method.
        print(f"the language is: {self.language}  the salary is: {self.salary}")


    
    @staticmethod
    def greet():
        print(f"good morning {aman.name}")

aman=Employee("aman",400000,"dsa")       #object created  (this all store in INIT function)
aman.name="aman"    #object or instance attribute

print(aman.name,aman.language,aman.salary)
aman.getInfo()
aman.greet()

#dubey=Employee()  #again object created again init function run



