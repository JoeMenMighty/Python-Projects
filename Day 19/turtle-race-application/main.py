from turtle import Turtle, Screen
import random


mighty_screen = Screen()
is_race_on = False

mighty_screen.setup(width=600, height=500)
player_answer = mighty_screen.textinput(title="Place Your Bet",
                                        prompt="Choose which turtle will win. Enter a color in the rainbow : ")

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

y_point = -100
for col in colors:
    mighty_turtle = Turtle(shape='turtle')
    mighty_turtle.color(col)
    mighty_turtle.penup()
    mighty_turtle.goto(x=-290, y=y_point)
    y_point += 40
    all_turtles.append(mighty_turtle)

if player_answer:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 270:
            is_race_on = False
            winner = turtle.pencolor()
            if player_answer == winner:
                print(f"Congratulations!!!!!...The {winner} turtle won.")
            else:
                print(f"You lost!!!!!. The {winner} turtle won..")
        rand_move = random.randint(1, 10)
        turtle.forward(rand_move)


mighty_screen.exitonclick()