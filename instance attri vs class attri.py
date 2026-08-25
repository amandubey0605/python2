# object or instance attributes,take priority(preference) over class attributes during assignment
# and retrieval
class Employee:
    name="aman"
    language="py"

s1=Employee()
s1.name="saloni"

print(s1.name,s1.language)   #it preffer object attribute instead of class attributes

#hera attributes are name,language