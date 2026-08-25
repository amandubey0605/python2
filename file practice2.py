# the game () function in a program lets a user play a game and returns the score as an integer. 
# you need to read a file 'Hi-score.txt' which is either blank or contains privious high
# score. you need to write a program to update a high score when ever the game() function breaks the
# hiscoregh 
import random     #This imports the random module so we can generate a random score.

def game():  #We are creating a function named game().
    print("You are playing the game....")   #Display a message

    score=random.randint(1,100)  #random.randint(1,100) means:
                                 # Generate a random number
                                 #Between 1 and 100
    
    print (f'your score is: {score}')  #Print the score


    #fetch the high score
    with open("Hi-score.txt","r") as f:  #Open the high-score file (It opens the file so we can read the previous high score.)
        hiscore=f.read()  #Read the file

        if(hiscore!=""):   #Check if the file is not empty
            hiscore= int(hiscore) #convert string high score in integer
        else:
            hiscore=0  #If empty

            #check for new high score   
    if(score> hiscore):   #Compare the scores
        print(f"your high score is: {score}")
        #write this high score to the file
        with open("Hi-score.txt","w") as f:  #Open the file in write mode(It replaces the old content with the new content.)
             f.write(str(score))  #Write the new high score
    return score  #This sends the score back from the function.
game() #call function(this starts the game)