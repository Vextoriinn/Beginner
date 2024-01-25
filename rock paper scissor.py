
from random import randint

t = ["rock", "paper", "scissors"]

computer = t[randint(0,2)]

player = False 

while player == False:
    player = input("rock, paper, scissors?")
    if player == computer:
        print("tie")
    elif player == "rock":
        if computer == "paper":
            print("You lose", computer, "covers", player)
        else:
            print("you win!", player, "smashes", computer)
    elif player == "paper":
        if computer == "scissor":
            print("You lose", computer, "cuts", player)
        else:
            print("you win!", player, "covers", computer)    
    elif player == "scissor":
            if computer == "rock":
                print("You win", computer, "smashes", player)
            else:
                print("you lose!", player, "cuts", computer)    
    else:
        print("invalid play, pick inside index.")  