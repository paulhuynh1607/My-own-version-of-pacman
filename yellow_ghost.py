from turtle import Turtle
import math
import random

YELLOW = "yellow"
MOVE = 10
degree = [270, 90]
START_POSITION = [0, 80]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
TURN = random.choice(degree)


class Yellow(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.left(90)
        self.goto(START_POSITION)



    def create(self):
        self.color(YELLOW)
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

    def is_close(self, other):
        a = self.ycor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))
        if distance < 75:
            return True
        else:
            return False

    def random_turn(self):
        self.right(TURN)
