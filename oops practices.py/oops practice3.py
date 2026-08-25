#Create a class with a class attribute a: create an object from it ant set 'a' directly using
# object.a=0.does it change the class attribute.(no it not change class attribute)

class change():
    a="aman" #class attribute


b=change()
print(f'firstly it is: {b.a}') #print the class attribute because instance attribute is not present.
b.a=0  # instance attribute is set here

print(f"after it is : {b.a}") #print the instance attribute because instance attribute is  present.
print(change.a) #print the class attribute.

'''b.a = 0 changes the attribute for object b, not the class attribute.

If you wanted to change the class attribute, you would write:
syntex-

Change.a = 0
 
Then all objects that don't have their own "a" would see 0.'''