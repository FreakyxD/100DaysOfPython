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


def player_turn():
    my_board.player_add_to_board()


def cpu_turn():
    print("CPU is thinking", end="", flush=True)
    _ = [print(".", end="", flush=True) or time.sleep(0.75) for _ in range(5)]
    my_board.cpu_add_to_board()


# todo ending condition - when either team plays the last turn
# todo only update a single playing board
def game():
    global game_over
    game_round = 1
    init_game()
    starting_player = determine_starter()
    my_board.display_board()

    if starting_player == "player":
        while not game_over:
            if game_round % 2 == 0:
                cpu_turn()
            else:
                player_turn()
            game_round += 1
            my_board.display_board()
    elif starting_player == "cpu":
        while not game_over:
            if game_round % 2 == 0:
                player_turn()
            else:
                cpu_turn()
            game_round += 1
            my_board.display_board()
    else:
        print("Error while determining starter!")
        game_over = True

        # game_over = True


game()
