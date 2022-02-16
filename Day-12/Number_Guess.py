# Imports
import random

from numpy import diff
from art import logo

# True Number
true_number = random.randint(1, 100)



# Check for too high or too low
def check_high_low(guess, actual):
    if guess > actual:
        return "Too High"
    else:
        return "Too Low"

# Get Number of Turns
def get_number_of_turns(difficulty):
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5

# Get Difficulty
def get_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    return difficulty

# Play Game
def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    turns = get_number_of_turns(get_difficulty())

    while turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        if guess == true_number:
            print(f"You guess the number correct {true_number}")
            exit(0)
        else:
            print(check_high_low(guess, true_number))
            turns = turns - 1

play_game()

