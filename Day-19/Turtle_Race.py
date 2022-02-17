# Imports
import random
from turtle import Turtle, Screen

# Screen Objects and Configurations
screen = Screen()
screen.setup(width=500, height=400)

# Get User Bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the rce? Enter a color: ")

# Check Race Status
is_race_on = False

# Colors for Turtle
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Turtle Object and Configurations
for turtle_index in range(0, 6):
    turtle_obj = Turtle(shape="turtle")
    turtle_obj.penup()
    turtle_obj.color(colors[turtle_index])
    turtle_obj.goto(x=-230, y=y_positions[turtle_index])

    all_turtles.append(turtle_obj)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False

            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
