from turtle import Turtle

RIGHT_BAR = (450, 0)
LEFT_BAR = (-450, 0)


class Paddle(Turtle):
    """Paddle class that creates a 20x100 paddle"""

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.move_to(position)

    def move_to(self, pos):
        """moves paddle to left or right side. move left or right as parameters"""
        if pos is 'right':
            self.goto(RIGHT_BAR)
        elif pos is 'left':
            self.goto(LEFT_BAR)

    def move_up(self):
        """Moves paddle up by 20px"""
        y_dir = self.ycor() + 20
        self.goto(self.xcor(), y_dir)

    def move_down(self):
        """Moves paddle down by 20px"""
        y_dir = self.ycor() - 20
        self.goto(self.xcor(), y_dir)
