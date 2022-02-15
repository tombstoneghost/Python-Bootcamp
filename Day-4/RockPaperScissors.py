# Imports
from random import randint

# Greetings
print("Welcome to the Rock, Paper and Scissors Game.")

# Options
print("The following are the notations for each\n0 - Rock\n1 - Paper\n2 - Scissors")

# Get User Choice
user_choice = int(input("Enter your play? "))

# Get System Choice
system_choice = randint(0, 2)

# Check for invalid input
if user_choice not in [0, 1, 2]:
    print("Invalid Input.")
    exit(0)

# Check for Draw
if user_choice == system_choice:
    print("Game Draw.")
# Check for other conditions
else:
    if user_choice == 0 and system_choice == 1:
        print("System Wins.")
    elif user_choice == 0 and system_choice == 2:
        print("User Wins.")
    elif user_choice == 1 and system_choice == 0:
        print("User Wins.")
    elif user_choice == 1 and system_choice == 2:
        print("System Wins.")
    elif user_choice == 2 and system_choice == 0:
        print("System Wins.")
    elif user_choice == 2 and system_choice == 1:
        print("User Wins.")
