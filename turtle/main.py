import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)

screen.tracer(0)
screen.listen()

player = Player()
score = Scoreboard()
cars = CarManager()
screen.onkey(player.go_up, 'Up')
screen.onkey(player.go_down, 'Down')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # move
    cars.move()

    cars.check_active()

    for car in cars.cars:
        if car.distance(player) < 10:
            score.game_over()
            screen.exitonclick()

    if player.ycor() > 280:
        score.increase_level()
        player.reset()
        cars.speed_up()

