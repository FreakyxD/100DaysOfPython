from turtle import Turtle


class LifeCounter(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.life = 3
        self.update_life()

    def update_life(self):
        self.clear()
        self.goto(-360, 265)
        self.write(f"❤{self.life}", align="center", font=("courier", 35, "normal"))

    def decrease_life(self):
        self.life -= 1
        self.update_life()

    def display_game_over(self):
        self.goto(0, 0)
        self.write("☠ GAME OVER ☠", align="center", font=("courier", 35, "normal"))

    def display_you_win(self):
        self.goto(0, 0)
        self.write("🏆 YOU WIN 🏆", align="center", font=("courier", 35, "normal"))
