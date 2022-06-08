import random
import turtle as t
from turtle import Screen

mensah_tutle = t.Turtle()
t.colormode(255)
mensah_tutle.pensize(10)

turn_angles = [90, 180, 270, 360]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rgb_random = (r, g, b)
    return rgb_random


# draw function to draw
def draw_in_direction():
    color = random_color()
    angle = random.choice(turn_angles)
    mensah_tutle.right(angle)
    mensah_tutle.color(color)
    mensah_tutle.forward(20)


# set turtle speed
mensah_tutle.speed(0)

# loop and draw randomly 50 times
for _ in range(10000):
    draw_in_direction()


mensah_screen = Screen()
mensah_screen.exitonclick()
