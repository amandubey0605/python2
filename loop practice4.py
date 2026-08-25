# WAP to find whether given number  is prime or not
n=int(input("enter the number"))

for i in range(2,n):
    if(n%i)==0:
        print(f'{n} is not a prime number')
        break
else:
     print(f'{n} is prime number')
print("code ended here")            