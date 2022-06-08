import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# create new player
player = Player()
player.start()

# create car manager
mighty_cars = CarManager()

# Create scoreboard
mighty_scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(key='Up', fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    mighty_cars.create_car()
    mighty_cars.move()

    # detect car collision
    for car in mighty_cars.all_cars:
        if car.distance(player) < 20:
            mighty_scoreboard.game_over()
            game_is_on = False

    # detect successful crossing
    if player.check_finish_status():
        mighty_cars.level_up()
        mighty_scoreboard.update_scoreboard()


screen.exitonclick()


