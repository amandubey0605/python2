#add a static method in problem 2, to greet the user with hello.
class Calculator:
    # n=int(input("enter the number: "))
    def __init__(self,n):
       self.n=n

    def square (self):
        print(f'square is {self.n*self.n}') 
    def cube (self):
        print(f'cube is {self.n*self.n*self.n}') 
    def square_root (self):
        print(f'square root is {round(self.n**0.5,2)}') 
    @staticmethod
    def hello():
        print("hello")    
n=int(input("Enter the number: "))
a=Calculator(n)
a.hello()
a.square()
a.cube()
a.square_root()
