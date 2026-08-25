# WAP to convert inches to centimeter
def convert(n):
    return n*2.54
n=int(input("enter the value in inche: "))
result=convert(n)
print(f'{n} inche is: {result} centimeter')