from turtle import  Screen
import turtle as turt
import random


circle_turtle = turt.Turtle()
turt.colormode(255)
circle_turtle.pensize(1)
circle_turtle.speed(0)


# random color generator
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rgb_random = (r, g, b)
    return rgb_random


# spirograph function
def draw_spirograph(gap_number):
    draw_number = int(360/gap_number)
    for _ in range(draw_number):
        color = random_color()
        circle_turtle.color(color)
        circle_turtle.circle(100)
        circle_turtle.setheading(circle_turtle.heading() + gap_number)


draw_spirograph(5)

circle_turtle_screen = Screen()
circle_turtle_screen.exitonclick()