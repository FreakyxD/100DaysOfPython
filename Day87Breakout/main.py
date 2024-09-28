import time
from turtle import Screen
from Day87Breakout.scoreboard import Scoreboard
from Day87Breakout.paddle import Paddle
from Day87Breakout.ball import Ball
from Day87Breakout.bricks import Brick

FPS = 30  # 30 is retro mode
if FPS == 60:
    sleep_time = 0.016
elif FPS == 30:
    sleep_time = 0.033
else:
    # new error
    raise ValueError("Invalid FPS value. Please enter 30 or 60.")

screen = Screen()
screen.setup(width=800, height=600)

# Disable window resizing
window = screen.getcanvas().winfo_toplevel()
window.resizable(False, False)

screen.title("Breakout")
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()

# create bricks
brick1 = Brick("aqua", 0, 0)  # todo debug

paddle = Paddle()

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

ball = Ball(FPS)

game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()

    ball.move()

screen.exitonclick()
