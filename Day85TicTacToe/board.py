import random

from teams import Teams
from wcwidth import wcswidth


def format_values(value):
    char_width = wcswidth(value)
    if char_width == 1:
        # padding 1
        return f" {value}  "
    elif char_width == 2:
        # padding 0
        return f" {value} "
    else:
        # handle error and exit program
        print(f"Error: Unexpected character width {char_width}. Program will terminate.")
        exit(1)


class Board(Teams):
    def __init__(self):
        super().__init__()
        self.board_values = [str(i + 1) for i in range(9)]

    def display_board(self):
        formatted_values = [format_values(value) for value in self.board_values]
        print(f"""
                       {formatted_values[0]}   |   {formatted_values[1]}   |   {formatted_values[2]}   
                    ----------+----------+----------
                       {formatted_values[3]}   |   {formatted_values[4]}   |   {formatted_values[5]}   
                    ----------+----------+----------
                       {formatted_values[6]}   |   {formatted_values[7]}   |   {formatted_values[8]}   
                    """)

    def is_occupied(self, board_index):
        if self.board_values[board_index - 1] == self.circle or self.board_values[board_index - 1] == self.cross:
            return True
        else:
            return False

    def player_add_to_board(self):
        shape = self.get_player_shape()

        while True:
            board_index = input("Pick a position (1-9): ")

            if not board_index.isdigit():
                print("Invalid input. Please enter a number between 1 and 9.")
                continue

            board_index = int(board_index)

            if board_index < 1 or board_index > 9:
                print("Invalid position. Please pick a position between 1 and 9.")
                continue

            if not self.is_occupied(board_index):
                self.board_values[board_index - 1] = shape
                break
            else:
                print("Position already occupied. Please pick another position.")

    # todo: only pick a number that is available
    def cpu_add_to_board(self):
        shape = self.get_cpu_shape()

        while True:
            cpu_board_index = random.randint(1, 9)
            if not self.is_occupied(cpu_board_index):
                self.board_values[cpu_board_index - 1] = shape
                break

    def debug_fill_board(self):
        available_positions = list(range(1, 10))

        for i in range(9):
            if i % 2 == 0:
                shape = self.get_player_shape()
            else:
                shape = self.get_cpu_shape()

            # Randomly select from the available positions
            board_index = random.choice(available_positions)
            self.board_values[board_index - 1] = shape

            # Remove the chosen position from the available list
            available_positions.remove(board_index)

        # Display the board after filling
        self.display_board()
