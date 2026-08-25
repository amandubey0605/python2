'''Q1 create a class(2-d vector) and use it to create another class representing a 3-d vector.'''
class Twovector():

    def __init__(self,i,j):
        self.i=i
        self.j=j
    
    def show(self):
        print(f'the vector is {self.i}i + {self.j}j')  

class Threevector(Twovector):
    def __init__(self,i,j,k): 
        super().__init__(i,j)
        self.k=k
    
    def show(self):
            print(f'the vector is {self.i}i + {self.j}j + {self.k}k')     

a= Twovector(2,3)
a.show()
b=Threevector(2,3,4)
b.show()

           
'''Inheritance gives the child access to the parent's methods and attributes, while super() lets us call the parent's methods/constructor explicitly.'''      
