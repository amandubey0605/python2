# WAP to print star pattern of first n lines of the following pattern using function.

def star_pattern(n):
    for i in range(n, 0, -1):
        print("*" * i)

n = int(input("Enter the number: "))
star_pattern(n)
