from turtle import Turtle

WHITE = "white"
MOVE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
START_POSITION = [0, 80]


class White(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.left(90)
        self.goto(START_POSITION)


    def create(self):
        self.color(WHITE)
        self.shape("triangle")

    def reset_ghost(self):
        self.goto(START_POSITION)

    def move(self):
        self.forward(MOVE)

    def up(self):
        if self.heading() != DOWN:
            self.setheading(UP)

    def down(self):
        if self.heading() != UP:
            self.setheading(DOWN)

    def turn_left(self):
        if self.heading() != RIGHT:
            self.setheading(LEFT)

    def turn_right(self):
        if self.heading() != LEFT:
            self.setheading(RIGHT)



