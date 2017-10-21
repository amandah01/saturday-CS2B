# Guess the Number Game
# A game by Amanda Huynh
#Sept 23, 2017

#import the random module
import random

#Game introduction
author = "Amanda Huynh"
print("Welcome to Guess the Number Game")
print("A game by {}. All Rights Reserved.".format(author))
print()
print("Please enter your name below:")
player = input()
print("Hello {}!".format(player))

#Play
correct_number = random.randint(1,20)
guess_number = 0
guesses = 0
max_guesses = 10
print("I am thinking of a number between 1 and 20")
while (guesses < max_guesses) and (correct_number != guess_number):
    print("Guesses left: {}".format(max_guesses - guesses))
    print("Enter your guess below:")
    guess_number = int(input())
    if guess_number < correct_number:
        print("Your guess is too low.")
        guesses += 1
        #penalty
    elif guess_number > correct_number:
        print("Your guess is too high.")
        guesses += 1
    else:
        print("Congrats! It took you {} guesses!".format(guesses + 1))
if guesses == max_guesses:
    print("You're out of guesses. You're THAT bad.")
    print("The correct number is {}.".format(correct_number)) 
