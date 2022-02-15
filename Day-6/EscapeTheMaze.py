'''
Maze Solver for Maze in Reeborg's World
'''

# Predefined Functions
def turn_left():
    print('Left')

def move():
    print("Move")

def front_is_clear():
    print("Front Clear")

def wall_in_front():
    print("Wall Front")

def right_is_clear():
    print("Clear Right")

def wall_on_right():
    print("Wall Right")

def at_goal():
    print("At Goal")


# Function to run Right
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# Solve the puzzle
while front_is_clear():
    move()

turn_left()


while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()


