#  function which call itself

# factorial(2)=2x1
# factorial(3)=3x2x1
# factorial(4)=4x3x2x1
# factorial(5)=5x4x3x2x1
# factorial(6)=6x5x4x3x2x1
# factorial(n)= nxn-1x............3x2x1

#factorial(n)=n*factorial(n-1)
def fact(n):
    if( n==0 or n==1):
        return 1
    if(n<0):  
        return "negative number"
    return n*fact(n-1)


n=int(input("enter the value of n: "))
print(f'factorial of n entered number is :{fact(n)}')  #this is also right
n=int(input("enter the value of n: " ))
print(f'factorial of n entered number is :{fact(n)}')
n=int(input("enter the value of n: "))
print(f'factorial of n entered number is :{fact(n)}')
n=int(input("enter the value of n: "))
print(f'factorial of n entered number is :{fact(n)}')
print("thanks")


#    OR
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

num = int(input("Enter the value of n: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num} is: {fact(num)}")

print("Thanks")