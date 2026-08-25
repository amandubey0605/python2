# solving a problem by creating object is one of the most popular approches in programming.this is called object-oriented programming.
# this concept focuses on using reusable code(Dry principle) 
#object(particular information) inside class and class is blank form(it has information to keep valid object)
class Employee:
    # name="aman"
    language="python"  #this is the class attribute jo v object banega class ke ander sab ka language yahi rahega jab tak khud se koi value assign nhi krte object attribute m
    salary="200000"
aman=Employee()       #object
aman.name="aman"    #object or instance attribute
print(aman.name,aman.salary)

viratkohli=Employee()
viratkohli.name="virat"

print(viratkohli.name,viratkohli.language,viratkohli.salary)


# here name is object attributes and salary and language are class attributes(they are directly belong to the class)