from .card import Card
import random


class Board:
    def __init__(self, board_size):
        if not isinstance(board_size, int):
            raise TypeError('Argument must be an even integer.')
        elif board_size % 2 != 0:
            raise ValueError('Argument must be even.')

        self.__grid = [[0]*board_size for i in range(board_size)]
        self.size = board_size

    # Special Methods

    def __iter__(self):
        return iter(self.__grid)

    def __getitem__(self, coord):   # board_instance[x, y]
        x, y = coord
        return self.__grid[x][y]

    def __setitem__(self, coord, value):  # board_instance[x, y] = value
        x, y = coord
        self.__grid[x][y] = value

    def __str__(self):
        result = ""
        for row in self:
            for card in row:
                if card.is_reveal:
                    result += (str(card) + " ")
                else:
                    result += ("? ")
            result += "\n"

        return result

    # Public Methods
    def populate(self):
        card_value_array = list(range(1, self.size**2 // 2 + 1)) * 2
        random.shuffle(card_value_array)

        for row in self:
            for idx in range(len(row)):
                row[idx] = Card(card_value_array.pop())

    def won(self):
        for row in self:
            for card in row:
                if not card.is_reveal:
                    return False

        return True

    def render(self):
        for row in self:
            for card in row:
                if card.is_reveal:
                    print(card, end=" ")
                else:
                    print("? ", end=" ")
            print()

    def valid_coord(self, x, y):
        return True if 0 <= x < self.size and 0 <= y < self.size else False
