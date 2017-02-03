#! /usr/bin/python3.5
# Random Guess 
# Trent Engler
# 5/14/16

import random
randnum = random.randint(1,100)
x=0
max=7
while x <= max:
    #print(randnum)
    print("Guess a random number between 1 and 100")
    guess = input("\nGuess " + str(x+1) + " of " + str(max) + "... ")
    if int(guess) > randnum:
        print("too high! ... Guess again")
        x+=1
    elif int(guess) < randnum:
        print("too low! ... Guess again")
        x+=1
    else:
       print("you got it! ... it was " + str(randnum))
       break