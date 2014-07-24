from random import *

#Variables
x = randrange(50)
playerGuess = 0
numberGuesses = 0

def mainLoop(z, y):
    while True:
        print ("Take a guess")
        z = input("> ")
        y += 1
        if z == x:
            print("You got it in " + str(y) + " guesses!")
            break
        elif z < x:
            print("Too Low")
        else:
            print("Too high")
        if y > 10:
            print("You used all your guesses.")
            print("The number I was thinking of is " + str(x))
            break
    
print("I'm thinking of a number between 0 and 50")
mainLoop(playerGuess, numberGuesses)
print("Thanks for Playing!")