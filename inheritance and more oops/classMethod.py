#Class method.
'''a class method is a method which is bound to the  class and not the object of the
class
syntex-- "@classmethod:" decorator is used to create a class method

(class method ek tarika hai hamlog ke pass ek method ke ander class ko directly acces krne kaa)'''

class Employee():
    a=1
    @classmethod  #ye bss  class ka method(attributes or properties) access krta hai na ke instance(object) atrribute ka
                  #issilyee ye 45 nhi 1 print krega agar "class method" use nhi krte to 45 print krta

    def Show(Cls):  #(class method uses Cls instead of self)
        print(f"The class attribute is: {Cls.a}")

o=Employee()
o.a=45

Employee.Show()