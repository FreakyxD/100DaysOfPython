from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.width(3)
        self.penup()
        self.hideturtle()

    def draw_line(self):
        for start_y in range(-300, 300, 40):
            print(start_y)
            self.goto(0, start_y)
            self.pendown()
            # draw line
            self.goto(0, start_y + 15)
            self.penup()
        print("done")
