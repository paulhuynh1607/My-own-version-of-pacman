from turtle import Turtle

START_POSITION = [0, -80]
MOVE_DISTANCE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.speed = 0.1
        self.penup()
        self.player()

    def player(self):
        self.goto(START_POSITION)
        self.color("yellow")
        self.shape("circle")
        self.setheading(0)

    def reset_p(self):
        self.player()
        self.speed = 0.1

    def move(self):
        self.forward(MOVE_DISTANCE)

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


