from art import logo
from board import Board

game_over = False

my_board = Board()


def init_game():
    my_board.print_teams()
    my_board.set_shape()
    my_board.print_teams()


def game():
    global game_over
    print(logo)

    init_game()
    while not game_over:
        #my_board.display_board()

        game_over = True


game()
