from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.speed = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 265)
        self.write(f"Score: {self.score}  Speed: {self.speed:.2f}", align="center", font=("courier", 35, "normal"))

    def increase_score(self, points):
        self.score += points
        self.update_scoreboard()
