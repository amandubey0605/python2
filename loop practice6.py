# WAP to calculate the factorial of given number using loop(while,for)
n= int(input("enter the number: "))

i=1
fact=1
while(i<=n):
    fact=fact*i 
    i+=1
print(f'factorial of {n} is: {fact}')


# or using for loop
n1=int(input("enter the number:  "))

factorial=1
for i in range(1,n+1):
    
    factorial=factorial*i
print(f'the factorial of {n} is : {factorial}') 

    #  OR
n2 = int(input("Enter the number: "))

factorial = 1

if n2 == 0 or n2 == 1:
    print(f"The factorial of {n1} is : 1")
else:
    for i in range(1, n2 + 1):
        factorial = factorial * i

    print(f"The factorial of {n2} is : {factorial}")


    