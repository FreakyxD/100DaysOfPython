from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1

        self.hideturtle()
        self.penup()

    def update_scoreboard(self):
        self.goto(-280, -280)
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT)

    def enter_next_level(self):
        self.level += 1

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg="GAME OVER", font=FONT, align="center")
