import math
import random

string_random_number = ""
website_link = "" # Insert the future website link here to 
#showcase your project on the interactive portfolio!
isVictory = False
num_guesses = 10

def printIntro():
    print("\nBagels, a deductive logic game.\nBy Nithin Rajesh " + website_link)
    print("\nI am thinking of a 3-digit number. Try to guess what it is.\nHere are some clues:\n     When I say:\tThat means:\n\tPico\t\tOne digit is correct but in the wrong position.\n\tFermi\t\tOne digit is correct and in the right position.\n\tBagels\t\tNo digit is correct.\nI have thought up a number.\n You have 10 guesses to get it.\n")


def getRandomNumber():
    random_number = str(random.randint(100, 999))
    return random_number

def checkGuess(guess, the_random_number):
    full_clue = ""
    if(guess == the_random_number):
        full_clue = "You got it!\n"
    else:
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

def playAgain():
    choice = ""
    while(choice != "yes" or choice != "no"):
        print("Please input either \"yes\" or \"no\".")
        choice = input("Do you want to play again? (yes or no)\n")
        choice = choice.lower()
        if(choice == "yes"):
            printIntro()
            playGame()
        else:
            print("Thanks for playing!")
            break

def playGame():
    guess = ""
    initial_counter_guess = 1
    string_random_number = getRandomNumber()
    num_guesses_left = 10
    while(guess != string_random_number):
        guess = input("Guess #" + str(initial_counter_guess) + ": ")
        if len(guess) != 3:
            print("Guess must be 3 digits long.")
            continue
        clue = checkGuess(guess, string_random_number)

        if(clue != "You got it!"):
            print(clue)
            initial_counter_guess += 1
            num_guesses_left -= 1
        else:
            print(clue)
            break

        if(initial_counter_guess > 10 and num_guesses_left == 0):
            print("You ran out of guesses! The number was " + string_random_number + "!")
            break