#extra works
n=int(input("enter the number: "))

factorial=1
for i in range(1,n+1):
    factorial=factorial*i
    
print(f"factorial of {n} is :{factorial}")  

#    OR
def greatest1(r,t,y):
    if(r>t and r>y):
        return r
    elif(t>y and t>y):
        return t
    else:
        return y
a=int(input("Enter the value:  "))    
b=int(input("Enter the value:  "))    
c=int(input("Enter the value:  "))    
result=greatest1(a,b,c)    
print(f"greatest number among three is: {result}") 

#    OR
def cal_sum(n):
    if(n==1):
        return 1
    Sum= n+cal_sum(n-1)
    return Sum
print("sum is: ",cal_sum(10))

#  practice by self
import random

def game():
    print("starting the game....")
    score=random.choice(1,100)
    print(f'your score is: {score}')

    with open("Hi-score.txt","r") as f:
        hiscore=f.read()

        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    if(score>hiscore):
        with open("Hi-score.txt","w")as f:
            print(f"your highest score is :{str(score)}")   
    return score
game()                  


    
