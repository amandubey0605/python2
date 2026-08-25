'''Write __str__() method to print the vector as follows: 7i + 8j + 10k assume vector of the dimension  for this problem.
'''
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x}i +{self.y}j + {self.z}k" 


v = Vector(7, 8, 10)

print(v)
