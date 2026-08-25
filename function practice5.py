# Write a recursive function to calculate the sun of first n natural number
def cal_sum(n):
    if (n==1):  #base condition (ye issilye lagate hai ki apka recursion hai wo infinitly ulta na chale)
        return 1
    return n+cal_sum(n-1)
n=int(input("enter the number: "))
result=cal_sum(n)
print(f'sum of first {n} natural number is: {result}')   

