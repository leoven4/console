from turtle import Turtle

STARTING_POSITION = [[0,0],[20,0],[40,0]]

class Snake:
    def __init__(self):
        self.init_length = 3
        self.blocks = []

        self.create_snake()
        self.game_on = True

    def create_snake(self):
        for i in range(self.init_length):
            self.add_block(STARTING_POSITION[i])

    def move(self):
        for block_num in range(len(self.blocks) - 1, 0, -1):
            new_x = self.blocks[block_num - 1].xcor()
            new_y = self.blocks[block_num - 1].ycor()
            self.blocks[block_num].goto(new_x, new_y)
        self.blocks[0].forward(20)

    def extend(self):
        x = self.blocks[-1].xcor()
        y = self.blocks[-1].ycor()
        self.add_block([x,y])

    def add_block(self, position):
        block = Turtle(shape='square')
        block.color('white')
        block.penup()
        block.goto(x=position[0], y=position[1])
        self.blocks.append(block)

    def up(self):
        if self.blocks[0].heading() != 270:
            self.blocks[0].setheading(90)

    def down(self):
        if self.blocks[0].heading() != 90:
            self.blocks[0].setheading(270)

    def left(self):
        if self.blocks[0].heading() != 0:
            self.blocks[0].setheading(180)

    def right(self):
        if self.blocks[0].heading() != 180:
            self.blocks[0].setheading(0)

    def head(self):
        return self.blocks[0]