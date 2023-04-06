from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.level = 1
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Level: {self.level}', align='center', font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'Level: {self.level}. GAME OVER!', align='center', font=FONT)
