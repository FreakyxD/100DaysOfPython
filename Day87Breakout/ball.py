from turtle import Turtle

class Ball(Turtle):
    def __init__(self, fps):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()

        if fps == 60:
            ball_speed = 1.67 # movement per frame at 60 fps
        else:
            ball_speed = 3.33 # movement per frame at 30 fps


        self.x_move = ball_speed
        self.y_move = ball_speed

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def increase_speed(self, boost):
        self.x_move += abs(boost) if self.x_move > 0 else -abs(boost)
        self.y_move += abs(boost) if self.y_move > 0 else -abs(boost)