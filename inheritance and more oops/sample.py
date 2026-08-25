class Animal:          # Parent class
    def eat(self):
        print("Animal is eating")


class Dog(Animal):     # Child class
    def bark(self):
        print("Dog is barking")


d = Dog()

d.eat()    # inherited from Animal
d.bark()   # Dog's own method