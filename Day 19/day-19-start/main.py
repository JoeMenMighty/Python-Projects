from turtle import Turtle, Screen

mighty_turtle = Turtle()
mighty_screen = Screen()


def move_forward():
    mighty_turtle.forward(30)


def move_backward():
    mighty_turtle.right(180)
    mighty_turtle.forward(30)


def move_clockwise():
    mighty_turtle.right(10)


def move_counter_clokwise():
    mighty_turtle.left(10)


def clear_drawing():
    mighty_turtle.clear()
    mighty_turtle.penup()
    mighty_turtle.goto(0, 0)  # can also use mighty_turtle.home()
    mighty_turtle.pendown()


mighty_screen.listen()
mighty_screen.onkey(key='f', fun=move_forward)
mighty_screen.onkey(key='b', fun=move_backward)
mighty_screen.onkey(key='c', fun=move_clockwise)
mighty_screen.onkey(key='a', fun=move_counter_clokwise)
mighty_screen.onkey(key='space', fun=clear_drawing)


mighty_screen.exitonclick()
