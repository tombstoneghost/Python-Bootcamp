# Imports
import random
import turtle

'''
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    rgb_colors.append((r, g, b))

print(rgb_colors)
'''

# Turtle Configuration
turtle.colormode(255)

# Turtle Object
turtle_obj = turtle.Turtle()

# Colors in the painting
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# Turtle Object Configuration
turtle_obj.speed("fastest")
turtle_obj.penup()

turtle_obj.setheading(225)
turtle_obj.forward(300)
turtle_obj.setheading(0)

# Dots
number_of_dots = 100

# Print Dots
for dot_count in range(1, number_of_dots + 1):
    turtle_obj.dot(20, random.choice(color_list))
    turtle_obj.forward(50)

    if dot_count % 10 == 0:
        turtle_obj.setheading(90)
        turtle_obj.forward(50)
        turtle_obj.setheading(180)
        turtle_obj.forward(500)
        turtle_obj.setheading(0)



screen = turtle.Screen()
screen.exitonclick()
