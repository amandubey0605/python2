# write a function to great a user with good day
#  function defination
def greet():
    user=input("enter your name: ")
    print("good day",user)
# function call
greet()  

#   OR
def greet2(name):
    gr="hello " +name
    return  gr          #function take a value and give the variable who want it (like value of gr goes in to a variable)
a=greet2("aman")
print(a)