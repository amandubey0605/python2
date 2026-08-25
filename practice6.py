#chapter string

# Q1.write a program to display a user entered name followed by good afternoon using input()function.
name=str(input("enter your name: "))

print(f'good afternoon,{name}')

# WAP to fill in a letter template given below with name and date.
letter='''dear <|NAME|>,
you are selected!
<|DATE|>'''

print(letter.replace("<|NAME|>","Aman").replace("<|DATE|>","06 may 2029"))
