from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("square")
        self.color("white")
        # default size is 20
        self.shapesize(stretch_wid=1, stretch_len=5) # 100x20 paddle
        self.penup()
        self.goto(0, -250)
        self.width(20)

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())