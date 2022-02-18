# Imports
import turtle
import pandas as pd

# Screen and it's configurations
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load CSV file
df = pd.read_csv("50_states.csv")

# Convert Dictionary Data into lists
states_list = df.state.to_list()
x_list = df.x.to_list()
y_list = df.y.to_list()

# Guessed States
guessed_states = []

while len(guessed_states) < 50:
    # Get Answer for the user
    answer_state = turtle.textinput(title=f"{len(guessed_states)}/50 States Guessed Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break
    if answer_state in states_list:
        guessed_states.append(answer_state)

        x_cor = x_list[states_list.index(answer_state)]
        y_cor = y_list[states_list.index(answer_state)]

        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.goto(x=x_cor, y=y_cor)
        state.write(answer_state)

# States to Learn
states_to_learn = list(set(states_list).difference(set(guessed_states)))

# Convert the States to learn in CSV
new_data = pd.DataFrame(states_to_learn)
new_data.to_csv("states_to_learn.csv")
