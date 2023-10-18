from turtle import Turtle
import random

COLORS = ["red", "orange", "teal", "green", "blue", "purple"]
# steps of 60
START_POSITIONS_Y = [-210, -150, -90, -30, 30, 90, 150, 210]
# Idea: increase car speed for all cars at once? main car loop?
#  or ensure that all cars get cleared upon reaching new level; then make sure the new ones are being
#  initialized with the new speed

STARTING_MOVE_DISTANCE = 5

# MOVE_INCREMENT my code was designed for 10, anything else looks off
# That's why I don't use increase_speed(); I increase spawn probability instead increase_difficulty()
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("square")
        self.penup()
        self.setheading(180)
        self.speed = STARTING_MOVE_DISTANCE
        self.shapesize(stretch_wid=1.2, stretch_len=2.5)
        self.random_start_y = random.choice(START_POSITIONS_Y)

        random_color = random.choice(COLORS)
        self.color(random_color)

        self.goto(315, self.random_start_y)

    def move_car(self):
        self.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
