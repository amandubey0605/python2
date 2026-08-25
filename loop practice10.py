# WAP to print multiplication table of n using for loops in reverse order.
n=int(input("enter the number: "))

for i in range(10,0,-1):
    print(f'{n}x{i} = {n*i}')
    

print("loop ends here")    

# we can also use for i in range(1,11):
                #  print(f'{n}x{i} = {n*(11-1)}')