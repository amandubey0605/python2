'''Q1Add 10 to every number'''

num=[1,2,3,4]

result=list(map(lambda x:x+10,num))

print(result)

#Q2.Convert Celsius into Fahrenheit

# Formula:
# \[
# F = (C \times 9/5) + 32
# \]
temp=[10,20,30,40]

result=list(map(lambda x:(x*9/5)+32,temp))

print(result)

#Q5. Extract the length of each word

words=["aman","saloni","kanak motkii","pandey chor"]

result=list(map(lambda x:len(x),words))

print(result)
