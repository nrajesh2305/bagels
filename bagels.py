import math
import random

num_guesses = 10
string_random_number = ""
website_link = "" # Insert the future website link here to 
#showcase your project on the interactive portfolio!

def printIntro():
    print("\nBagels, a deductive logic game.\nBy Nithin Rajesh " + website_link)
    print("\nI am thinking of a 3-digit number. Try to guess what it is.\nHere are some clues:\n     When I say:\tThat means:\n\tPico\t\tOne digit is correct but in the wrong position.\n\tFermi\t\tOne digit is correct and in the right position.\n\tBagels\t\tNo digit is correct.\nI have thought up a number.\n You have 10 guesses to get it.\n")


def getRandomNumber():
    random_number = random.randint(100, 999)
    string_random_number = str(random_number)
    return random_number

def checkGuess(guess, the_random_number):
    full_clue = ""
    tempCount = 0
    if len(guess) != 3:
        return "Guess must be 3 digits long."
    for i in range(3):
        if guess[i] in the_random_number and the_random_number[i] == guess[i]:
            full_clue += "Fermi "
        elif guess[i] in the_random_number and the_random_number[i] != guess[i]:
            full_clue += "Pico "
        else:
            if i == 2 and len(full_clue) == 0:
                full_clue = "Bagels"
                break
    return full_clue.strip()

