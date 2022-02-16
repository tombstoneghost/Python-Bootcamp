# Imports
import random
from art import logo, vs
from game_data import data

A = {}
B = {}

# Get A and B
def get_A_B():
    global A, B

    A = random.choice(data)
    B = random.choice(data)

# Show Options
def show():
    print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}")
    print(vs)
    print(f"Against B: {B['name']}, {B['description']}, from {B['country']}")

# Get Correct Answer
def get_correct_answer():
    if A['follower_count'] > B['follower_count']:
        return "A"
    else:
        return "B"

# Play Game
def play_game():
    print(logo)

    score = 0
    end_of_game = False

    while not end_of_game:
        get_A_B()
        show()

        correct_answer = get_correct_answer()

        answer = input("Who has more followers? Type 'A' or 'B': ").upper()

        if answer == correct_answer:
            score = score + 1
            print(f"You're right! Current Score: {score}")
        else:
            print(f"You're wrong!  Current Score: {score}")
            print("Thanks for playing")
            end_of_game = True

play_game()
