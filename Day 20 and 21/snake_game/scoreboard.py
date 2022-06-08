from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('courier', 15, 'normal')
GAME_OVER_FONT = ('courier', 20, 'normal')
X_MID = -4.5


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as high_score_file:
            game_high_score = high_score_file.read()
            self.high_score = int(game_high_score)
        self.color('white')
        self.penup()
        self.goto(x=X_MID, y=275)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        new_score = f'Score : {self.score} High Score : {self.high_score}'
        self.write(arg=new_score, move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(f'{self.high_score}')

        self.score = 0
        self.write_score()

    # def game_over(self):
    #     self.goto(X_MID, 0)
    #     self.write(arg="GAME OVER !!!!", move=False, align=ALIGNMENT, font=GAME_OVER_FONT)

    def update_score(self):
        self.score += 1
        self.write_score()