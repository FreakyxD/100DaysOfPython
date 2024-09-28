from turtle import Turtle


class Brick(Turtle):
    COLOR_POINTS = {
        "red": 7,
        "orange": 7,
        "yellow": 4,
        "green": 4,
        "aqua": 1,
        "blue": 1,
    }

    def __init__(self, color, x, y):
        super().__init__()

        if color not in self.COLOR_POINTS:
            raise ValueError("Invalid brick color")

        self.shape("square")
        self.color(color)
        # default size is 20
        self.shapesize(stretch_len=2.75, stretch_wid=0.70)  # 55x14 brick

        # self.penup()
        self.x = x
        self.y = y
        self.goto(self.x, self.y)

        self.hit = False
