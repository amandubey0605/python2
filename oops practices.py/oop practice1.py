#create a class "programmer" for storing information of few programmers working at microsoft
class Programmer():
     Company="microsoft"
     def __init__(self,name,age,skill,salary):
          self.name=name
          self.age=age
          self.skill=skill
          self.salary=salary
     @staticmethod
     def greet():
          print("thank you")   
          
         
Emp1=Programmer("aman",21,"python full stack developer",400000)
Emp2=Programmer("sam",24,"python",200000)
Emp3=Programmer("karan",28,"java",150000)

#from here
print(f'First programmer details:company: {Emp1.Company} ,name: {Emp1.name}, age: {Emp1.age}, skill: {Emp1.skill},salary:{Emp1.salary}')
Emp1.greet()
print(f'Second programmer details:company: {Emp2.Company}, name: {Emp2.name}, age: {Emp2.age}, skill: {Emp2.skill},salary: {Emp2.salary}')
Emp2.greet()

print(f'Third programmer details: company: {Emp3.Company},name: {Emp3.name}, age: {Emp3.age}, skill: {Emp3.skill},salary: {Emp3.salary}')
Emp3.greet()
#to here we can also use loop

# Create a list of all programmers
#programmers = [Emp1, Emp2, Emp3]

# Loop through each programmer

# for emp in programmers:
#     print(f'Company: {emp.Company}, Name: {emp.name}, Age: {emp.age}, Skill: {emp.skill}, Salary: {emp.salary}')
#     emp.greet()


#  OR
'''# Create a class "Programmer" for storing information
# of programmers working at Microsoft

*(from here to)

class Programmer:
    Company = "Microsoft"

    def __init__(self, name, age, skill, salary):
        self.name = name
        self.age = age
        self.skill = skill
        self.salary = salary

    @staticmethod
    def greet():
        print("Thank you")


# Creating programmer objects
Emp1 = Programmer("Aman", 21, "Python Full Stack Developer", 400000)
Emp2 = Programmer("Sam", 24, "Python", 200000)
Emp3 = Programmer("Karan", 28, "Java", 150000)


# Store all objects in a list
programmers = [Emp1, Emp2, Emp3]


# Using loop to print details
for emp in programmers:
    print(f"Company: {emp.Company}")
    print(f"Name: {emp.name}")
    print(f"Age: {emp.age}")
    print(f"Skill: {emp.skill}")
    print(f"Salary: {emp.salary}")
    
    emp.greet()
    print()  # Adds an empty line  (to here)*
'''