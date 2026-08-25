# WAF to print multiplication table of given number.
def table(n):
    if n==0:
        return 0
    for i in range(1,11,1):
        print(f' {n} x {i} = {n * i}')
        
       
n=int(input("enter the number: "))
print(f'multiplication of {n} = {table(n)}')
    