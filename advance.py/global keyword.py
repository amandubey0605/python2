'''
'global' keyword is used to modify the variable outside of the current scope(function etc..)
'''

a=89 # global variable (we can use it in function or ouside of function(not inside function))

def fun():
    global a #(2)  (changed the value of global 'a' it changes or modify global variables)
    a=3 #local variable of a function
    print(a)

#print(a) (1)
fun()    
print(a)