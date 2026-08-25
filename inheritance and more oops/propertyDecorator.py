# # The @property decorator allows us to use a method like an attribute.

# # Normally, if we have a method, we call it using ():

# # class Student:
# #     def get_name(self):
# #         return "Aman"

# # s = Student()

# # print(s.get_name())  # () is required

# # But with @property, we can call the method without ():
# class Student:
#     @property
#     def name(self):
#         return "Aman"

# s = Student()

# print(s.name)  # No ()

# Output:

# Aman
# 🧠 Simple idea

# Without @property:

# s.name()

# With @property:

# s.name

# So, @property makes a method behave like an attribute when you access it.

'''study'''
class Employee():
    a=1
    @classmethod 

    def Show(Cls): 
        print(f"The class attribute is: {Cls.a}")

    @property    
    def name(self):  #name ek function hai jisme ek logic chalega lekin aisa dikhao ki ye ek propertty hai
                      #yani ki user self.name karaye aur ham 
        return  f"{self.fname} {self.lname}" # return function chala ke ye return value(o.name) me rakh do

    @name.setter   #3. user ko ye pta na chale ke itni mahanet ho rhi hai user bss (o.name) bs ye likhe yahi hai abstraction and incapsulation ka matlab
                      #incapsulation(we can't see implimantation details) or bhut sare kaam krne wale component ko ek unit me pack kr diya 
                      #abstraction-hidding implimentation details
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
  

o=Employee()
o.a=45

o.name="aman dubey" #2. aur main o.name="some thing " karu to us value ko leke(3)first name and last name set kr do
print(o.name)

Employee.Show()
