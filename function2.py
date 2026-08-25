# two type of function 1. built_ in function (len,range,print etc..) and 2. user defined function(func1,n,a,etc..)

# function with argument
def greet(name,ending):
    print("good day",name)
greet("aman","thank you")
greet("saloni","thank you")
greet("kanak","thank you") 

#   OR
def cal_sum(n):
    if (n==1):  #base condition (ye issilye lagate hai ki apka recursion hai wo infinitly ulta na chale)
        return 1
    return n+cal_sum(n-1)
n=10
print(f'sum of first {n} natural number is: {cal_sum(10)}')   




















