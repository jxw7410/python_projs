from board import Board
import os_func as sys
import re as regex
import time


class Game:
    def __init__(self):
        self.board = Board(8)
        self.board.populate()
        self.is_over = False
        self.previous_card = None
        self.player_turn = True

    # Public Methods
    def play(self):
        while not self.is_over:
            self.__render()
            user_input = input(
                "Please provide coordinates, such as 2, 3 etc:\n")

            try:
                x, y = self.__parse_coordinates(user_input)
            except Exception as error:
                print(error)
                input('Press any key to continue...\n')
            else:
                if self.board.valid_coord(x, y):
                    self.process_board(x, y)
                else:
                    print('Coordinate input exceed bounds of Board.')
                    input('Press any key to continue...\n')

    def process_board(self, x, y):
        self.board[x, y].reveal()
        if not self.previous_card:
            self.previous_card = self.board[x, y]

        elif self.previous_card.value != self.board[x, y].value:
            self.__render_no_match()
            self.previous_card.hide()
            self.board[x, y].hide()
            self.previous_card = None
            self.player_turn = False if self.player_turn else True

        if self.board.won():
            self.is_over = True

    # Private Methods
    def __parse_coordinates(self, input):
        num_array = regex.findall(r'\d+', input.replace(',', " "))

        if len(num_array) != 2:
            raise ValueError("Input contains less or more than 2 numbers")

        return map(lambda arg: int(arg), num_array)

    def __render(self):
        sys.clear()
        print(f"It's player { '1' if self.player_turn else '2'}'s turn.\n")
        self.board.render()

    def __render_no_match(self):
        self.__render()
        print('Card does not match!')
        time.sleep(1)
