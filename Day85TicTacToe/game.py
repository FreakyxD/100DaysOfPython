from art import logo
from board import Board

game_over = False

my_board = Board()


def game():
    global game_over
    print(logo)

    while not game_over:
        my_board.display_board()

        my_board.get_shapes()
        my_board.set_shape()
        my_board.get_shapes()

        game_over = True


game()
