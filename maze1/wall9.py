from turtle import Turtle


class Wall9(Turtle):
    def __init__(self):
        super().__init__()

    def create(self):
        self.color("blue")
        self.shape("square")
        self.shapesize(stretch_wid=6, stretch_len=6)
