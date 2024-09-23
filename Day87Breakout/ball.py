from turtle import Turtle

class Ball(Turtle):
    def __init__(self, fps):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()

        # Set initial ball speed based on FPS
        if fps == 60:
            ball_speed = 1.67
        else:
            ball_speed = 3.33

        self.x_move = ball_speed
        self.y_move = ball_speed
        self.speed_factor = 1.0  # Multiplier for speed, starting at 1.0

    def move(self):
        """Move the ball by updating its position based on current speed."""
        new_x = self.xcor() + self.x_move * self.speed_factor
        new_y = self.ycor() + self.y_move * self.speed_factor
        self.goto(new_x, new_y)

    def bounce_x(self):
        """Reverse the horizontal direction of the ball."""
        self.x_move *= -1

    def bounce_y(self):
        """Reverse the vertical direction of the ball."""
        self.y_move *= -1

    def increase_speed(self):
        """Increase ball speed by scaling up the speed factor."""
        self.speed_factor *= 1.1  # Increase speed by 10%