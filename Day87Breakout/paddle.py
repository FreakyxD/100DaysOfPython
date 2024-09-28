from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("square")
        self.color("white")
        # default size is 20
        self.shapesize(stretch_len=3, stretch_wid=0.60)  # 60x12 paddle
        self.penup()
        self.goto(0, -250)

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
