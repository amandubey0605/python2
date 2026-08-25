# WAP to find whether  a given username contains less then 10 character or not
name=input("enter your name:  ")

if(len(name)<=10):
    print(f'{name}, contains less then 10 character in it: {len(name)}')
else:
    print(f'{name},contains more then 10 character in it: {len(name)}')    


#Q5.WAP to find out whether the given name is present in a list or not
user_names=["aman","saolni","kanak","supriya"]

name=input("Enter your name:  ")

if(name in user_names):
    print("yes,your name is in the list")
else:
    print("your name is not in the list")    