import time
from turtle import Screen
from Day87Breakout.scoreboard import Scoreboard
from Day87Breakout.paddle import Paddle
from Day87Breakout.ball import Ball
from Day87Breakout.bricks import Brick

BRICK_STRETCH_WID = 0.80

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


def lay_bricks():
    brick_height = 20 * BRICK_STRETCH_WID
    brick_rows = 6
    score_counter_height = 40

    # Calculate the starting y-coordinate for the top brick row
    starting_y = (screen.window_height() / 2) - score_counter_height

    bricks = []
    colors = ["#FF3300", "#FF9900", "#FFFF33", "#33FF33", "#00FFFF", "#3333FF"]
    color_index = 0
    for row in range(brick_rows):
        current_color = colors[color_index]
        color_index += 1

        # Calculate the y-coordinate for the current row
        y = starting_y - (brick_height * row)
        for col in range(20):  # number of bricks fitting in the 800 screen width
            x = -385 + (col * 40)
            new_brick = Brick(BRICK_STRETCH_WID, current_color, x, y)
            bricks.append(new_brick)
    return bricks


def check_collision(brick_to_check):
    pass


list_of_bricks = lay_bricks()

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
    for brick in list_of_bricks:
        check_collision(brick)

screen.exitonclick()
