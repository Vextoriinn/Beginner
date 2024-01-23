#Draft of Number Guesser Game

import random  

lowest_number = 1
highest_number = 500
max_guesses = 8 

random_number = random.randint(lowest_number, highest_number)

def applied_guesses():
    while True:
        guess = int(input("guess a number between", {lowest_number and highest_number}))
        if lowest_number <= guess <= highest_number:
            return guess
        elif lowest_number > guess > highest_number:
            print("invalid guess, make sure guess is within", {lowest_number and highest_number})
        else:
            print("Not a valid number.")

def validate_guess(guess, random_number):
    if guess == random_number:
        return("Correct")
    elif guess < random_number:
        return("too low")
    else:
        return ("too high")
    
def play_number_guesser():
    Attempts = 0 
    won = False

    while attempts < max_guesses:
        attempts = + 1
        guess = applied_guesses()
        result = validate_guess(guess, random_number)

    if result == "Correct":
        print("You guessed the random number! You did this in {attempts} attempts.")
        won = True
        break
    else:
        print("{result}. guess again.")

    if not won:
        print("No more guesses left, the number was {random_number}")


play_number_guesser()
     
    




