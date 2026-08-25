# WAP to print the following star pattern:*
                                     #   **
                                    #  *****   
                                         
rows = 3

for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")

    # Print stars
    for k in range(i * (i + 1) // 2):
        print("*", end="")

    print()
#     OR
n=int(input("Enter the value: "))

for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")