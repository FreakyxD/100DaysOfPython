from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.penup()

        self.x_movement_speed = 3.33  # positive moves right
        self.y_movement_speed = 3.33  # positive moves up
        self.bounce_count = 0

    def move(self):
        new_x = self.xcor() + self.x_movement_speed
        new_y = self.ycor() + self.y_movement_speed
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_movement_speed *= -1
        self.track_bounces()

    def bounce_y(self):
        self.y_movement_speed *= -1
        self.track_bounces()

    def track_bounces(self):
        """Track the number of bounces and increase speed after 5th and 13th bounce."""
        self.bounce_count += 1
        if self.bounce_count in [5, 13]:
            self.increase_speed()

    def increase_speed(self):
        # increase speed by 10%, but cap it at 10
        self.x_movement_speed = min(self.x_movement_speed * 1.05, 10) if self.x_movement_speed > 0 else max(
            self.x_movement_speed * 1.05, -10)
        self.y_movement_speed = min(self.y_movement_speed * 1.05, 10) if self.y_movement_speed > 0 else max(
            self.y_movement_speed * 1.05, -10)

    def reset_position(self):
        self.goto(0, 0)
