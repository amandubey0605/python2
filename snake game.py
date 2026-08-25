'''
1 for snake 
-1 for  water
0 for gun
'''
import random

Computer= random.choice([-1,0,1])
yourchoice=input("Enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
reverseDict ={1:"Snake",-1:"Water",0:"Gun"}

you=youDict[yourchoice]

print(f"you chose {reverseDict[you]}\nComputer chose {reverseDict[Computer]}")

if(Computer== you):
    print("Draw")

else:
        # long method
    # if(Computer==-1 and you==1): -2
    #     print("You Win!")
        
    # elif(Computer==-1 and you==0):   -1
    #       print("You Lose!")

    # elif(Computer==1 and you==-1):  2
    #     print("You Lose!")

    # elif(Computer==1 and you==0): 1
    #     print("You Win!")
 
    # elif(Computer==0 and you==-1):  1
    #     print("You Win!")

    # elif(Computer==0 and you==1): -1
    #     print("You Lose!")
    # else:
    #     print("Something went wrong!") 

           #  OR
        if((Computer- you)==-1 or (Computer-you)== 2):
              print("You Lose!")

        else:
              print("You Win!")
              print("Congratulation")            


