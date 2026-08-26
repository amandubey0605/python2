#THE PERFECT GUESS
'''we are going to write' a program that generate a random number and asks the user to 
guess it.

if the players guess is higher than the actual number, the program displays "lower number please".
similarly , if the users guess is too low,the programm prints"higher number please"when the user guesses the correct number,
the program display the number of guesses the player used to arrive at the number.'''
import random

n = random.randint(1, 100)

guesses = 0

while True:

    a = int(input("Guess the number: "))

    guesses += 1

    if a > n:
        print("Lower number please!")

    elif a < n:
        print("Higher number please!")

    else:
        print("You guessed it!")
        print("Number of guesses:", guesses)
        break