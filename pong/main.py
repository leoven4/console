from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.listen()
screen.tracer(0)

paddle_l = Paddle((350, 0))
screen.onkey(paddle_l.go_up, 'Up')
screen.onkey(paddle_l.go_down, 'Down')

paddle_r = Paddle((-350, 0))
screen.onkey(paddle_r.go_up, 'a')
screen.onkey(paddle_r.go_down, 'z')

ball = Ball()
score = Score()
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision ball
    if ball.ycor() > 270 and ball.going_up:
        ball.bounce_y()

    if ball.ycor() < -270 and not ball.going_up:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()


screen.exitonclick()


