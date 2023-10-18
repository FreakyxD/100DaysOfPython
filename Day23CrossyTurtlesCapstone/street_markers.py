from turtle import Turtle

FINISH_LINE_Y = 260


class Lanes(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("square")
        self.color("black")
        self.width(3)
        self.penup()
        self.hideturtle()

        # lane spacing
        for start_y in range(-240, 300, 60):
            print(start_y)
            self.goto(-300, start_y)
            self.penup()
            # draw lane
            for start_x in range(-300, 300, 110):
                self.goto(start_x, start_y)
                self.pendown()
                self.goto(start_x + 45, start_y)
                self.penup()

        # finishing line
        self.color("orange")
        self.goto(-300, FINISH_LINE_Y + 10)
        self.pendown()
        self.goto(300, FINISH_LINE_Y + 10)

        print("done")
