from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

    def increase_speed(self, boost):
        # or def bounce_y(self):
        #     self.y_move *= -1.1
        #
        # def bounce_x(self):
        #     self.x_move *= -1.1
        if self.x_move < 0:
            self.x_move -= boost
        else:
            self.x_move += boost

        if self.y_move < 0:
            self.y_move -= boost
        else:
            self.y_move += boost

