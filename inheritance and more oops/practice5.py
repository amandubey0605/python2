'''Write a class"vector" repersenting a vector of n dimensions.Overloading the + and * operator "+"operators which calculates the sum and the dot(.)product of them'''
class Vector():
    def __init__(self, value,value2):
        self.value=value
        self.value2=value2

    def __add__(self, other):
        return (self.value + other.value,
               self.value2 + other.value2)

    def __mul__(self,other):
        return (self.value *other.value)+ (self.value2 * other.value2)   #first × first
                                                                          # +
                                                                          # second × second

    def __str__(self):
       return f'[{self.value } + {self.value2}]'
A=Vector(1,2)       
B=Vector(4,5)

print(f'The sum is : {A + B}')
print(f'The multiplication is : {A *B}')

