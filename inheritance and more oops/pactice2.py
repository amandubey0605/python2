'''Q2 create a pet class from a class "animals" and further create a class "dog" from "pet".and a method bark to class Dog'''

class Animal():
    def __init__(self,lion,goat):
        self.lion=lion
        self.goat=goat

class Pet(Animal):
    def __init__(self, lion, goat,peacock):
        super().__init__(lion, goat)
        self.peacock=peacock

class Dog(Pet):
    def __init__(self, lion, goat, peacock):
        super().__init__(lion, goat, peacock)

    def bark(self):
        print(f'A dog bark,{self.lion} wake up and {self.goat} goat eats grass and {self.peacock} peacock do dance')    

a=Animal("sher","bakri")
b=Pet("sher","bakri","mor")
c=Dog("sher","bakri","mor")
c.bark()


  #OR
'''class Animal:
    pass

class Pet(Animal):
    pass

class Dog(Pet):
    def bark(self):
        print("Dog is barking")


d = Dog()
d.bark()'''  

        