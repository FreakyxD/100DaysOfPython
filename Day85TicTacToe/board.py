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
        self.board_values = [str(i+1) for i in range(9)]


    def display_board(self):
        formatted_values = [format_values(value) for value in self.board_values]
        print(f"""
                       {formatted_values[0]}   |   {formatted_values[1]}   |   {formatted_values[2]}   
                    ----------+----------+----------
                       {formatted_values[3]}   |   {formatted_values[4]}   |   {formatted_values[5]}   
                    ----------+----------+----------
                       {formatted_values[6]}   |   {formatted_values[7]}   |   {formatted_values[8]}   
                    """)

    # todo human readable index conversion
    def add_to_board(self, index, shape):
        while True:
            if self.board_values[index] == self.circle or self.board_values[index] == self.cross:
                print("There is already a marker!")
            else:
                self.board_values[index] = shape
                break

    def cpu_add_to_board(self, shape):
        cpu_choice = random.randint(1, 9)
        self.board_values[cpu_choice - 1] = shape
