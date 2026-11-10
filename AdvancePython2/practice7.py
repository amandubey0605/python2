'''Convert numbers into strings

Use map() to convert all numbers into strings.'''

num=[1,2,3,4,5]

s=list(map(lambda x:str(x),num))

print(f"Here converted num to str:{s}")

'''Let's break it down:
- num → Your original list of integers.
- map() → Applies a function to every element.
- lambda x: → Takes each element one by one.
- str(x) → Converts each integer into a string.
- list() → Converts the map object into a list.
For example:
Original	Converted
1 (int)	'1' (str)
2 (int)	'2' (str)
3 (int)	'3' (str)
4 (int)	'4' (str)
5 (int)	'5' (str)

'''