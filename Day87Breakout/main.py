import time
from turtle import Screen
from Day87Breakout.scoreboard import Scoreboard
from Day87Breakout.lifecounter import LifeCounter
from Day87Breakout.paddle import Paddle
from Day87Breakout.ball import Ball
from Day87Breakout.bricks import Brick

BRICK_STRETCH_WID = 0.80

FPS = 90  # 30 is retro mode
sleep_time = {60: 0.016, 30: 0.033, 90: 0.011}.get(FPS, None)
if sleep_time is None:
    raise ValueError("Invalid FPS value. Please enter 30, 60, or 90.")

screen = Screen()
screen.setup(width=800, height=600)

# disable window resizing
window = screen.getcanvas().winfo_toplevel()
window.resizable(False, False)

screen.title("Breakout")
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()
life_counter = LifeCounter()

# paddle setup
paddle = Paddle(screen.window_width())


def lay_bricks():
    brick_height = 20 * BRICK_STRETCH_WID
    brick_rows = 6
    score_counter_height = 40

    # calculate the starting y-coordinate for the top brick row
    starting_y = (screen.window_height() / 2) - score_counter_height

    bricks = []
    colors = ["#FF3300", "#FF9900", "#FFFF33", "#33FF33", "#00FFFF", "#3333FF"]
    color_index = 0
    for row in range(brick_rows):
        current_color = colors[color_index]
        color_index += 1

        # calculate the y-coordinate for the current row
        y = starting_y - (brick_height * row)
        for col in range(20):  # number of bricks fitting in the 800 screen width
            x = -385 + (col * 40)
            new_brick = Brick(BRICK_STRETCH_WID, current_color, x, y)
            bricks.append(new_brick)
    return bricks


def collided_with_brick(brick_to_check):
    if ball.distance(brick_to_check) < 16:
        return True
    return False


def bounce_angle(my_ball, my_paddle):
    min_x_speed = 1  # Ensure x movement is not too small
    max_speed = 15 # never exceed the speed of the paddle
    # calculate the difference between the ball's position and the paddle's center
    offset = my_ball.xcor() - my_paddle.xcor()

    # if the ball hits near the center of the paddle, bounce straight up
    if abs(offset) < 3:
        my_ball.x_movement_speed = 0
    else:
        # adjust the angle based on how far the ball is from the center
        angle_multiplier = min(abs(offset) / (my_paddle.paddle_width / 2), 1)  # normalize within range [0, 1]

        # determine the new speed while preserving direction
        base_speed = max(abs(my_ball.x_movement_speed), min_x_speed) * (1 + angle_multiplier)
        new_speed = base_speed if offset > 0 else -base_speed  # positive for right, negative for left

        # ensure the speed does not exceed the maximum speed
        if abs(new_speed) > max_speed:
            new_speed = max_speed if new_speed > 0 else -max_speed

        # assign the new speed to the ball's x movement
        my_ball.x_movement_speed = new_speed

    # reverse the y direction to make the ball bounce upward
    my_ball.bounce_y()


# initialize bricks and ball
list_of_bricks = lay_bricks()
ball = Ball()


# paddle movement function
def move_paddle():
    if paddle.move_left_pressed:
        paddle.move_left()
    if paddle.move_right_pressed:
        paddle.move_right()

    # repeat the paddle movement frequently (every 10 ms)
    screen.ontimer(move_paddle, 10)


# bind key presses to paddle movement
screen.listen()
screen.onkeypress(paddle.start_move_left, "Left")
screen.onkeyrelease(paddle.stop_move_left, "Left")
screen.onkeypress(paddle.start_move_right, "Right")
screen.onkeyrelease(paddle.stop_move_right, "Right")

# start the paddle movement timer
move_paddle()

win = None
# main game loop
while life_counter.life > 0:
    time.sleep(sleep_time)
    screen.update()

    ball.move()

    # detect collision with paddle
    if ball.distance(paddle) < 45 and ball.ycor() < -235:
        bounce_angle(ball, paddle)

    # detect collision with bricks
    for brick in list_of_bricks:
        if collided_with_brick(brick):
            ball.bounce_y()
            list_of_bricks.remove(brick)
            brick.hideturtle()

            # increase score based on brick color
            scoreboard.increase_score(brick.get_brick_value())

    # detect collision with walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # detect collision with top wall
    if ball.ycor() > 260:
        ball.bounce_y()
    elif ball.ycor() < -300:
        # ball missed the paddle
        life_counter.decrease_life()
        ball.hideturtle()
        del ball
        time.sleep(2)
        ball = Ball()
        ball.move()

    if len(list_of_bricks) == 0:
        # force the screen to update to reflect the change immediately
        screen.update()
        win = True
        break

time.sleep(1)
if win:
    life_counter.display_you_win()
else:
    life_counter.display_game_over()

screen.exitonclick()
