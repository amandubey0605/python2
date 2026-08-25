# Q3. write a program to detect double spaces in a string

name="aman  dubey is a good boy"

print(f'double space found at:{name.find("  ")}')

# or
text = input("Enter a string: ")

position = text.find("  ")

if position != -1:
    print("Double spaces found at index:", position)
else:
    print("No double spaces found.")