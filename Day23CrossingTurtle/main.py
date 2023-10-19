import time
import random
from turtle import Screen
from player import Player
from street_markers import Lanes
from car_manager import Car
from scoreboard import Scoreboard

# BUG if high probability like 0.9
#  can just limit to a max value that works
#  seems to only occur if it's that high when game starts, can progress to level +10 easily
PROBABILITY_THRESHOLD = 0.1  # 10%
ACTIVE_CAR_GOAL = 25
active_cars = []

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Crossy Turtles")

player = Player()
lanes = Lanes()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.hop, key="Up")


def spawn_car(n):
    for _ in range(n):
        while True:
            new_car = Car()
            car_conflict_found = False
            for active_car in active_cars:
                # if any active car too close to new car
                if new_car.ycor() == active_car.ycor():
                    if new_car.distance(active_car) < 70:
                        car_conflict_found = True
                        destroy_car(new_car, already_in_list=False)
                        break
            # if no active car close to new car
            if not car_conflict_found:
                active_cars.append(new_car)
                return


def destroy_car(car_object, already_in_list):
    if already_in_list:
        active_cars.remove(car_object)
    car_object.hideturtle()
    del car_object


def increase_difficulty(probability):
    """...by increasing spawning probability if it's not already at 100%"""
    if probability < 1.0:
        return probability + 0.1


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_scoreboard()

    # level complete
    if player.is_at_finish_line():
        scoreboard.enter_next_level()
        PROBABILITY_THRESHOLD = increase_difficulty(PROBABILITY_THRESHOLD)
        print(f"percentage: {PROBABILITY_THRESHOLD}")

        player.reset_position()

    # spawn car with randomness
    print(f"Active Cars: {len(active_cars)}")
    random_value = random.random()
    if random_value < PROBABILITY_THRESHOLD:
        if len(active_cars) < ACTIVE_CAR_GOAL:
            spawn_car(1)

    # main car control
    for car in active_cars:
        # movement
        if car.xcor() > -320:
            car.move_car()
        else:
            # reached end of screen
            destroy_car(car, already_in_list=True)

        # collision detection
        if player.distance(car) < 30:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
