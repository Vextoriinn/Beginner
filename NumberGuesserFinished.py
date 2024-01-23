#Draft of Number Guesser Game


import random  

lowest_number = 1
highest_number = 10
max_guesses = 10 

random_number = random.randint(lowest_number, highest_number)

def applied_guess():
    while True:
        try:
            guess = int(input(f"guess a number between {lowest_number} and {highest_number}: "))
            if lowest_number <= guess <= highest_number:
                return guess
            else:
                print("invalid guess, make sure guess is within the range.")
        except ValueError:
            print("Not a valid number, enter a number.")

def validate_guess(guess, random_number):
    if guess == random_number:
        return "Correct"
    elif guess < random_number:
        return"too low"
    else:
        return "too high"
    
def play_numberguesser():
    attempts = 0 
    won = False

    while attempts < max_guesses:
        attempts += 1
        guess = applied_guess()
        result = validate_guess(guess, random_number)

        if result == "Correct":
            print(f"You guessed the random number! You did this in {attempts} attempts.")
            won = True
            break
        else:
            print(f"{result}. guess again.")

    if not won:
        print(f"No more guesses left, the number was {random_number}")

if __name__ == "__NumberGuesser__":
    print("Lets play the Number guesser game!")

play_numberguesser()
    




