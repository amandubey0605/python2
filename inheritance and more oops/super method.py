#super()method is used to access the method of a super class in the derived class
#super() is used in a child class to access the methods or constructor of its parent class.
#Syntex-- "super().__init__()"

class Employee():  #parents or base or super


      a=1
class Programmer(Employee):
    def __init__(self):
         print("Constructer of programmer")

      
    b=2


class manager(Programmer): #child or drived or sub
    def __init__(self):#constructer of manager  (drived or child class)
             #in this program manager ka super class(parent class) Programmer hai      
         super().__init__() #constructer of parent(pogrammer) agar manager ka constructor chale to programmer(parent)calss ka v constructor chale.
                   #Agar manager ka constructor chale, aur hum super().__init__() likhen, to Programmer (parent class) ka constructor bhi chalega.
                    
         print("Constructor of manager")
    c=3


o=Employee()
print(o.a)

o=Programmer()
print(o.a,o.b)

o=manager()
print(o.a,o.b,o.c)

'''Constructor of manager starts
        ↓
super().__init__()
        ↓
Programmer's __init__() runs
        ↓
"Constructer of programmer"
        ↓
Back to manager
        ↓
"Constructor of manager"'''