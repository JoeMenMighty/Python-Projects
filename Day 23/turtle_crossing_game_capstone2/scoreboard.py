from turtle import Turtle

FONT = ("Courier", 24, "normal")
STARTING_LEVEl = 0


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.level = STARTING_LEVEl
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 260)
        self.write(f"Level : {self.level}", move=False, align='center', font=FONT)
        self.increase_level()

    def increase_level(self):
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align='center', font=FONT)
