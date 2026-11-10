'''Write a Student Marksheet Generator.

Requirements:
1. Input student name.
2. Input marks in 3 subjects.
3. Calculate total marks.
4. Calculate percentage (assume each subject is out of 100).
5. Display everything using format().
Expected output:
------ STUDENT MARKSHEET ------
Name: Rahul
Python: 85
Java: 90
SQL: 80
Total Marks: 255
Percentage: 85.0%
-------------------------------
'''
name=input("Enter the name of Student: ")
sub1=int(input("Enter the Python marks: "))
sub2=int(input("Enter the Java marks: "))
sub3=int(input("Enter the SQL marks: "))

total_marks=sub1+sub2+sub3
percentage=(total_marks/300)*100

student="Name: {}\nPython: {}\nJava: {}\nSQL: {}\nTotal Marks: {}\nPercentage: {}%".format(name,sub1,sub2,sub3,total_marks,percentage)

print(student)



