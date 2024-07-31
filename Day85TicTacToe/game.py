import random
import time

from art import logo
from board import Board

game_over = False

my_board = Board()


def init_game():
    print(logo)
    my_board.print_teams()
    my_board.set_shape()
    my_board.print_teams()


def determine_starter():
    print("Tossing coin to determine the first player", end="", flush=True)
    _ = [print(".", end="", flush=True) or time.sleep(1) for _ in range(5)]
    print()  # Move to the next line after dots

    if random.randint(0, 1) == 0:
        print(f"You go first!")
        return "player"
    else:
        print(f"CPU goes first!")
        return "cpu"


def game():
    global game_over
    init_game()

    while not game_over:
        my_board.display_board()
        # todo: player, cpu = my_board.get_shapes()

        starting_player = determine_starter()
        if starting_player == "player":
            pass
        elif starting_player == "cpu":
            pass
        else:
            print("Error while determining starter!")
            game_over = True

        game_over = True


game()
