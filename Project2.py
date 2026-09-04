#THE PERFECT GUESS
'''we are going to write' a program that generate a random number and asks the user to 
guess it.

if the players guess is higher than the actual number, the program displays "lower number please".
similarly , if the users guess is too low,the programm prints"higher number please"when the user guesses the correct number,
the program display the number of guesses the player used to arrive at the number.'''
import random

n = random.randint(1, 100)

guesses = 0

while True:  #So the loop keeps executing again and again indefinitely until something stops it.


    a = int(input("Guess the number: "))

    guesses += 1

    if a > n:
        print("Lower number please!")

    elif a < n:
        print("Higher number please!")

    else:
        print("You guessed it! the number is : ",n)
        print("Number of guesses:", guesses)
        break

'''So the loop keeps executing again and again indefinitely until something stops it.

In our guessing game, this stops it:

break

So think of it like:

while True → keep asking for guesses → break → stop when the correct number is guessed.

🎯 Now answer Q2 and Q3:

Q2: Why do we use:

guesses += 1

Q3: Why do we use:

break

Explain in your own words. Don't worry about grammar—we care about your logic. 💪'''    