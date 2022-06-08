from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

mighty_screen = Screen()
mighty_screen.setup(width=600, height=600)
mighty_screen.bgcolor('black')
mighty_screen.title('Mighty Snake Game')
mighty_screen.tracer(0)

mighty_snake = Snake()
mighty_food = Food()
mighty_scoreboard = ScoreBoard()

mighty_screen.listen()
mighty_screen.onkeypress(fun=mighty_snake.move_up, key='Up')
mighty_screen.onkeypress(fun=mighty_snake.move_down, key='Down')
mighty_screen.onkeypress(fun=mighty_snake.move_left, key='Left')
mighty_screen.onkeypress(fun=mighty_snake.move_right, key='Right')


is_game_on = True

while is_game_on:
    mighty_screen.update()
    time.sleep(0.10)
    mighty_snake.move()

    # detect collision with food
    if mighty_snake.snake_head.distance(mighty_food) < 15:
        mighty_snake.extend_snake()
        mighty_food.refresh()
        mighty_scoreboard.update_score()

    # detect collision with wall
    x_cod = mighty_snake.snake_head.xcor()
    y_cod = mighty_snake.snake_head.ycor()
    if x_cod > 295 or x_cod <= -295 or y_cod > 270 or y_cod < -280:
        mighty_scoreboard.reset()
        mighty_snake.reset()


    # detect collision with tail
    for segment in mighty_snake.snake[1:]:
        if mighty_snake.snake_head.distance(segment) < 10:
            mighty_scoreboard.reset()
            mighty_snake.reset()




mighty_screen.exitonclick()