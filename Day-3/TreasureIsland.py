# Greeting
from turtle import right


print("Welcome to Treasure Island\nYour mission is to find the treasure")

# Ask for Direction
direction = input("Where you want to go? Left or right? ")

# Check for correct direction
if direction.lower() == "right":
    print("Game Over.")
    exit(0)
else:
    swim_wait = input("Would you like to swim or wait? ")

    if swim_wait.lower() == "swim":
        print("Game Over.")
        exit(0)
    else:
        door = input("Which door would you like to go in? Red, Yellow or Blue? ")

        if door.lower() == "red" or door.lower() == "blue":
            print("Game Over.")
            exit(0)
        else:
            print("You Win!")
