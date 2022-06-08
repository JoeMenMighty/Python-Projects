from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard


mighty_screen = Screen()
mighty_screen.setup(width=1000, height=600)
mighty_screen.bgcolor('black')
mighty_screen.title('Mighty Pong Game')
mighty_screen.tracer(0)

right_paddle = Paddle('right')
left_paddle = Paddle('left')
mighty_ball = Ball()
mighty_score = ScoreBoard()

mighty_screen.listen()


mighty_screen.onkeypress(key='Up', fun=right_paddle.move_up)
mighty_screen.onkeypress(key='Down', fun=right_paddle.move_down)
mighty_screen.onkeypress(key='w', fun=left_paddle.move_up)
mighty_screen.onkeypress(key='s', fun=left_paddle.move_down)


is_game_on = True

while is_game_on:
    time.sleep(mighty_ball.speed_of_ball)
    mighty_screen.update()

    # Detect wall collision
    if mighty_ball.ycor() > 270 or mighty_ball.ycor() < -270:
        mighty_ball.bounce_wall()

    # Detect paddle collision
    if mighty_ball.xcor() > 420 and mighty_ball.distance(right_paddle) < 50 or \
            mighty_ball.xcor() < -420 and mighty_ball.distance(left_paddle) < 50:
        mighty_ball.bounce_paddle()

    # Detect restart and score
    if mighty_ball.xcor() > 520 and mighty_ball.distance(right_paddle) > 50:
        mighty_score.left_update()
        mighty_ball.restart()

    elif mighty_ball.xcor() < -520 and mighty_ball.distance(right_paddle) > 50:
        mighty_score.right_update()
        mighty_ball.restart()

    mighty_ball.move_to()


mighty_screen.exitonclick()
