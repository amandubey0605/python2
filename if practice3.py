# write a program to find out whether a student has passed or failed if it requres a totle 40% and at least 33% in each subject to pass assume 3 subjects and take marks as an input from the user.

sub1=int(input("enter the marks: "))
sub2=int(input("enter the marks: "))
sub3=int(input("enter the marks: "))

total_percentage=((sub1+sub2+sub3)/300)*100

if(total_percentage>=40 and sub1>=33 and sub2>=33 and sub3>=33):
    print("you are pass: ",round(total_percentage,2))
else:
    print("please come next year:",total_percentage)



# round(number, ndigits)  round() is used to round a number to the nearest integer or to a specified number of decimal places.
# number → The number you want to round.
# ndigits (optional) → Number of decimal places.