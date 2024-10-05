from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, screen_width):
        super().__init__()

        self.screen_width = screen_width - 67.5
        self.shape("square")
        self.color("white")
        # default size is 20
        self.shapesize(stretch_len=4.5, stretch_wid=0.60)  # 90x12 paddle
        self.paddle_width = self.shapesize()[0] * 20
        self.penup()
        self.goto(0, -250)

        # state to track key presses
        self.move_left_pressed = False
        self.move_right_pressed = False

    def move_left(self):
        # only allow movement if the paddle is within the screen width
        if self.xcor() - (self.paddle_width / 2) > -self.screen_width / 2:
            new_x = self.xcor() - 15
            self.goto(new_x, self.ycor())

    def move_right(self):
        # only allow movement if the paddle is within the screen width
        if self.xcor() + (self.paddle_width / 2) < self.screen_width / 2:
            new_x = self.xcor() + 15
            self.goto(new_x, self.ycor())

    def start_move_left(self):
        self.move_left_pressed = True

    def stop_move_left(self):
        self.move_left_pressed = False

    def start_move_right(self):
        self.move_right_pressed = True

    def stop_move_right(self):
        self.move_right_pressed = False
