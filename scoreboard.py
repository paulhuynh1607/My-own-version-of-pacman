from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.goto(0, 250)
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", font=FONT, align=ALIGNMENT)


    def reset_player(self, person, difficulty):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0
        with open("leaderboard.txt", mode="w") as data:
            if self.high_score > self.score:
                data.write(f"{person}: {self.high_score} difficulty: {difficulty}\n")
        self.clear()
        self.update_scoreboard()


    def increase(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
