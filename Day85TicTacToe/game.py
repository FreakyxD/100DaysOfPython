import random
import time
import numpy as np

from art import logo
from board import Board

my_board = Board()


def init_game():
    print(logo)
    my_board.print_teams()
    my_board.set_shape()
    my_board.print_teams()


def determine_starter(debug_enabled):
    if debug_enabled:
        delay = 0
    else:
        delay = 1
    print("Tossing coin to determine the first player", end="", flush=True)
    _ = [print(".", end="", flush=True) or time.sleep(delay) for _ in range(5)]
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


def check_win_condition(debug_enabled):
    b_vals = my_board.board_values
    matrix = np.array(b_vals).reshape(3, 3)

    main_diagonal = np.diag(matrix)
    anti_diagonal = np.diag(np.fliplr(matrix))

    first_row = matrix[0]
    second_row = matrix[1]
    third_row = matrix[2]

    first_column = matrix[:, 0]
    second_column = matrix[:, 1]
    third_column = matrix[:, 2]

    if debug_enabled:
        print("main diagonal", main_diagonal)
        print("anti diagonal", anti_diagonal)
        print("Row 1:", first_row)
        print("Row 2:", second_row)
        print("Row 3:", third_row)
        print("Column 1: ", first_column)
        print("Column 2: ", second_column)
        print("Column 3: ", third_column)

    all_things_to_check = (main_diagonal, anti_diagonal, first_row, second_row, third_row, first_column, second_column,
                           third_column)


    for shapes_list in all_things_to_check:
        all_same = np.unique(shapes_list).size == 1
        if all_same:
            # only one symbol in list --> Winner
            if shapes_list[0] == my_board.player:
                return "You"
            else:
                return "CPU"
    return "none"


def game():
    game_over = False
    game_round = 1
    debug_enabled = False
    init_game()
    starting_player = determine_starter(debug_enabled)
    my_board.display_board()

    if debug_enabled:
        my_board.debug_fill_board()
        print(check_win_condition(debug_enabled))
    else:
        if starting_player == "player":
            while not game_over:
                if game_round % 2 == 0:
                    cpu_turn()
                else:
                    player_turn()
                game_round += 1
                my_board.display_board()

                winner = check_win_condition(debug_enabled)
                if winner != "none":
                    print(f"GAME OVER! {winner} won!")
                    game_over = True
        elif starting_player == "cpu":
            while not game_over:
                if game_round % 2 == 0:
                    player_turn()
                else:
                    cpu_turn()
                game_round += 1
                my_board.display_board()

                winner = check_win_condition(debug_enabled)
                if winner != "none":
                    print(f"GAME OVER! {winner} won!")
                    game_over = True


game()
