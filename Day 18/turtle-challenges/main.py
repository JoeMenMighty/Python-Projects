from turtle import Turtle, Screen
import random


mighty_turtle = Turtle()
mighty_turtle.shape("turtle")
mighty_turtle.pensize(10)

# # draw a square
# for _ in range(4):
#     mighty_turtle.forward(100)
#     mighty_turtle.right(90)

# # draw a dashed line
# for _ in range(50):
#     mighty_turtle.forward(10)
#     mighty_turtle.penup()
#     mighty_turtle.forward(10)
#     mighty_turtle.pendown()


# draw shapes to overlay
color_palette = ['red', 'blue', 'green', 'yellow', 'DeepPink', 'orange', 'DarkViolet',
                 'chocolate', 'coral', 'GreenYellow', 'LightBlue', 'IndianRed', 'LightSeaGreen',
                 'gold', 'ForestGreen', 'DodgerBlue', 'navy', 'purple', 'LimeGreen', 'sienna',
                 'NavyBlue', 'peru', 'LawnGreen', 'firebrick', 'red2', 'green3', 'red4', 'red3']

turn_angles = [90, 180, 270, 360]
# turn_angles = [60, 120, 180, 240]
# turn_angles = [15, 45, 75, 105]

# # draws 3 - 10 sided shapes overlaying them
# def draw_shape(num_of_sides):
#     for i in range(num_of_sides):
#         mighty_turtle.color(color)
#         mighty_turtle.forward(100)
#         mighty_turtle.left(shape_angle)
#
#
# for _ in range(3, 10):
#     color = random.choice(color_palette)
#     shape_angle = 360 / _
#     draw_shape(_)


# draw function to draw
def draw_in_direction():
    color = random.choice(color_palette)
    angle = random.choice(turn_angles)
    mighty_turtle.right(angle)
    mighty_turtle.color(color)
    mighty_turtle.forward(20)

# set turtle speed
mighty_turtle.speed(0)

# loop and draw randomly 50 times
for _ in range(10000):
    draw_in_direction()


mighty_screen = Screen()
mighty_screen.exitonclick()
