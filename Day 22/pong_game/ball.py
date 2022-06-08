from turtle import Turtle
import random

RAND_DIRECTION = [-1, 1]


class Ball(Turtle):
    """Ball class that creates a white ball on screen"""
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed_of_ball = 0.1

    def move_to(self):
        """Function moves ball in some direction"""
        # cord_increment = random.randint(-10, 10)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        """Function changes direction of ball when it meets a wall"""
        self.y_move *= -1

    def bounce_paddle(self):
        """Function changes direction when it hits the paddle"""
        self.x_move *= -1
        self.speed_of_ball *= 0.99

    def restart(self):
        self.speed_of_ball = 0.1
        self.goto(0, 0)
        self.x_move *= -1
        rand_direction = random.choice(RAND_DIRECTION)
        self.y_move *= rand_direction
