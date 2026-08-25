# WAP to convert celsius into fahrenheit((9/5)xc +32) using function
def cels_to_fahh(c):
    f=(9/5)*c + 32
    return f
celsius=float(input("Enter the temprature in celsius: "))
fahrenheit=cels_to_fahh(celsius)
print(f"The temperature in fahrenheit is: {round(fahrenheit,2)}")

# round(number, ndigits)  round() is used to round a number to the nearest integer or to a specified number of decimal places.
# number → The number you want to round.
# ndigits (optional) → Number of decimal places.


# Q3. how do you prevent a python print function to print a new line at the end.
# using end function | print("abcd",end="") |it prevent new line
print("aman")
print("man")
print("an",end="")
print("n",end="")
