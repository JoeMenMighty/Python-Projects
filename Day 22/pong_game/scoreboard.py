from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 200)
        self.write(self.left_score, move=False, align='center', font=('courier', 70, 'normal'))
        self.goto(200, 200)
        self.write(self.right_score, move=False, align='center', font=('courier', 70, 'normal'))

    def right_update(self):
        self.right_score += 1
        self.update_scoreboard()

    def left_update(self):
        self.left_score += 1
        self.update_scoreboard()

