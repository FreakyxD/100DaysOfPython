from turtle import Turtle


class Ball(Turtle):
    def __init__(self, fps):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()

        if fps == 60:
            ball_speed = 1.67  # Movement per frame at 60 fps
        else:
            ball_speed = 3.33  # Movement per frame at 30 fps

        self.x_move = ball_speed
        self.y_move = ball_speed
        self.bounce_count = 0  # To track the number of bounces

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1
        self.track_bounces()

    def bounce_y(self):
        self.y_move *= -1
        self.track_bounces()

    # todo Additionally, the ball could also speed up when it hit certain rows of bricks,
    #  specifically the blue or green rows near the top of the screen.
    def track_bounces(self):
        """Track the number of bounces and increase speed after 5th and 13th bounce."""
        self.bounce_count += 1
        if self.bounce_count in [5, 13]:  # Increase speed after 5th and 13th bounce
            self.increase_speed()

    def increase_speed(self):
        """Increase ball speed by scaling up both x and y moves."""
        self.x_move *= 1.1
        self.y_move *= 1.1
