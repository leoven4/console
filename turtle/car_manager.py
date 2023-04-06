from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
N_CARS = 10

class CarManager(Turtle):
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        for i in range(N_CARS):
            self.create_car()

    def create_car(self):
        car = Turtle(shape='square')
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.color(COLORS[randint(0, 5)])
        x = randint(-280, 280)
        y = randint(-280, 280)
        car.goto(x, y)
        self.cars.append(car)

    def create_car_at_beg(self):
        car = Turtle(shape='square')
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.color(COLORS[randint(0, 5)])
        y = randint(-280, 280)
        car.goto(280, y)
        self.cars.append(car)

    def move(self):
        for i in range(len(self.cars)):
            new_x = self.cars[i].xcor() - MOVE_INCREMENT
            self.cars[i].goto(new_x, self.cars[i].ycor())

    def check_active(self):
        for i in range(len(self.cars)):
            if self.cars[i].xcor() < - 200:
                self.cars[i].hideturtle()
                self.cars.remove(self.cars[i])
                self.create_car_at_beg()

    def speed_up(self):
        self.speed += MOVE_INCREMENT