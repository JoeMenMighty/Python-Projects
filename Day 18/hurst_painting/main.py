from turtle import Turtle, Screen
import turtle as turt
import random

color_palette = [(14, 19, 40), (169, 59, 35), (201, 161, 104),
 (234, 239, 235), (138, 163, 195), (232, 205, 90), (47, 12, 8), (35, 11, 21), (70, 96, 129), (174, 154, 36),
 (164, 50, 68), (17, 45, 29), (188, 138, 152), (208, 68, 83), (148, 32, 21), (69, 115, 88), (158, 171, 158),
 (42, 50, 101), (203, 90, 73), (131, 35, 58), (218, 177, 183), (80, 81, 25), (39, 84, 37), (84, 111, 178),
 (224, 176, 172), (173, 189, 214), (40, 73, 75)]

mighty_turtle = turt.Turtle()
turt.colormode(255)
mighty_turtle.speed(0)
mighty_turtle.hideturtle()


# def draw filled circle
def draw_filled_circle(circle_radius, numb_steps):
    """Function takes a circle radius and constructs a filled circle"""
    y_cord = -200
    for _ in range(numb_steps):
        mighty_turtle.penup()
        mighty_turtle.goto(-200, y_cord)
        for i in range(numb_steps):
            # generates random colors
            color = random.choice(color_palette)
            mighty_turtle.dot(circle_radius, color)
            mighty_turtle.forward(40)
        y_cord += 40


# draw a dashed line
draw_filled_circle(20, 10)

mighty_screen = Screen()
mighty_screen.exitonclick()