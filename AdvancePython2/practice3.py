'''Write a Python program that takes three variables:
product = "Laptop" price = 45000  discount = 10


Use the format() function to print:
Product: Laptop
Original Price: 45000
Discount: 10%

Bonus: Calculate the final price after applying the 10% discount and print it too.


'''

product=input("Enter the name of product: ")

original_price=int(input("Enter the Price: "))

discount= 10

final_price=int(original_price-(discount/100)*original_price)

laptop_details="product: {}\noriginal_price: {}\nDiscount: {}%\nAfter_Discount price: {}".format(product,original_price,discount,final_price)

print(laptop_details)

