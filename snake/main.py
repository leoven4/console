from turtle import Screen
from Snake import Snake
from Food import Food
from Score import Score
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
snake = Snake()
screen.update()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


food = Food()
score = Score()

while snake.game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head().distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head().xcor() > 290 or snake.head().xcor() < -290 or snake.head().ycor() > 290 or snake.head().ycor() < -290:
        score.game_over()
        snake.game_on = False
        screen.exitonclick()

    # Detect collision with tail
    for block in snake.blocks[1:]:
        if snake.head().distance(block) < 10:
            game_on = False
            # score.game_over()

