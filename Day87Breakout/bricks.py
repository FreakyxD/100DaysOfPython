from turtle import Turtle


class Brick(Turtle):
    COLOR_POINTS = {
        "#FF3300": 7,  # Red
        "#FF9900": 7,  # Orange
        "#FFFF33": 4,  # Yellow
        "#33FF33": 4,  # Green
        "#00FFFF": 1,  # Aqua (Cyan)
        "#3333FF": 1,  # Blue
    }

    def __init__(self, stretch_wid, color, x, y):
        super().__init__()

        if color not in self.COLOR_POINTS:
            raise ValueError("Invalid brick color")

        self.shape("square")
        self.color(color)
        self.hex_color = color

        # start debug
        # self.pencolor("red")
        # self.pensize(2)
        # self.pendown()
        # end debug

        # default size is 20
        self.shapesize(stretch_len=2, stretch_wid=stretch_wid)  # 40x16 brick

        self.penup()
        self.x = x
        self.y = y
        self.goto(self.x, self.y)

        self.hit = False

    def get_brick_value(self):
        return self.COLOR_POINTS[self.hex_color]
