from turtle import Turtle


class Wall1(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-210, 150)

    def create(self):
        self.color("blue")
        self.shape("square")
        self.shapesize(stretch_wid=9, stretch_len=3)
