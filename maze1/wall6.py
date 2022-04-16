from turtle import Turtle


class Wall6(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-120, -180)

    def create(self):
        self.color("blue")
        self.shape("square")
        self.shapesize(stretch_wid=6, stretch_len=6)
