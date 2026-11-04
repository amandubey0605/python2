'''
Q2.Write a program to input name , marks, phone number of a student and format it
using using the format function like below :

"THe name of the student is aman, his marks are 80 and phone number is 999999988"
'''

student="Name of student:{},\nMarks obtained:{},\nPhone number:{}".format("Aman",80,6207297518)

print(student)

'''
Q3. Write a Python program to print the following using the format() function:
My name is Rahul.
I am 21 years old.
I scored 85.5 marks in Python.


Use variables instead of directly putting values inside format().

Try it yourself. I'll check your logic and code like a mentor! 💪
'''
name="Rahul"
age=21
marks=85.5

student2="My name is {}.\nI am {} years old.\nI scored {} marks in python".format(name,age,marks)

print(student2)
