'''Q6. Find even numbers'''

num=[1,2,3,4,5,6,7,8,9,10]

result=list(filter(lambda x:x%2==0,num))

print(f"even number among them are:{result}")

#Q7. Find numbers greater than 50
num=[10,60,30,80,45,90,20]

result2=list(filter(lambda y:y>50,num))

print(result2)

#Q3. Find words starting with A
words = ["Apple", "Banana", "Avocado", "Mango", "Apricot"]# Expected output:['Apple', 'Avocado', 'Apricot']


result3=list(filter(lambda x:x.startswith("A"),words))

print(result3)

#Q4. Find palindrome words
words = ["madam", "python", "level", "hello", "radar"]

result4=list(filter(lambda x:x==x[::-1],words))
print(result4)

#Q5Your next question (Q4):

'''Find all numbers divisible by both 3 and 5 using filter() and lambda.
numbers = [10, 15, 20, 30, 45, 50, 60, 75]# Expected output:[15, 30, 45, 60, 75]

Hint: Use the modulus operator %.'''
numbers = [10, 15, 20, 30, 45, 50, 60, 75]

result5=list(filter(lambda x:x%3==0 and x%5==0,numbers))

print(result5)

