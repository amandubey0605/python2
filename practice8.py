# chapter 3
# Q4.replace double spaces in single space in a problem 3
name="aman  dubey is a good boy"

print(name.replace("  "," "))
        # or
text = input("Enter a string: ")

position = text.replace("  "," ")

if position != -1:
    print( position)
else:
    print("not possible")        
