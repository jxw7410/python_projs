from .piece import Piece
from .piece_types.null_piece import NullPiece
from src.utils.constants import Const


class Board:
    def __init__(self):
        self.__grid = [
            [NullPiece((1,1), 'N')] * Const.BOARD_SIZE for i in range(Const.BOARD_SIZE)]

    # Special Methods
    def __iter__(self):
        return iter(self.__grid)

    def __getitem__(self, coord):
        x, y = coord
        return self.__grid[x][y]

    def __setitem__(self, coord, value):
        x, y = coord
        self.__grid[x][y] = value

    def __str__(self):
        ret = ""
        for row in self:
            for col in row:
                ret += (str(col) + " ")
            ret += "\n"
        return ret

    # Public Methods
    def initialize(self):
        self.__grid[0] = [Piece(self, (0, 0), Const.WHITE), Piece(self, (0, 1), Const.WHITE), Piece(self, (0, 2), Const.WHITE),
                          Piece(self, (0, 3), Const.WHITE), Piece(self, (0, 4), Const.WHITE), Piece(self, (0, 5), Const.WHITE),
                          Piece(self, (0, 6), Const.WHITE), Piece(self, (0, 7), Const.WHITE)]

        self.__grid[7] = [Piece(self, (7, 0), Const.BLACK), Piece(self, (7, 1), Const.BLACK), Piece(self, (7, 2), Const.BLACK),
                          Piece(self, (7, 3), Const.BLACK), Piece(self, (7, 4), Const.BLACK), Piece(self, (7, 5), Const.BLACK),
                          Piece(self, (7, 6), Const.BLACK), Piece(self, (7, 7), Const.BLACK)]

        # for c_idx in range(Const.BOARD_SIZE):
        #     self[1, c_idx], self[6, c_idx] = None, None

    def move_piece(start_pos, end_pos):
        self[start_pos], self[end_pos] = self[end_pos], self[start_pos]
