#format method (String) replace by f string

'''format the values inside the string into a desired output.
syntax-
template.format(p1,p2...)

example-
"{} is a good {}".format("harry","boy")
"{1} is a good {0}.format("harry","boy")
'''

# a="{} is a good {}".format("Aman","boy")
a="{1} is a good {0}".format("Aman","boy")
print(a)