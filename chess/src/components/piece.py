from src.utils.slideable import Slideable
from src.utils.constants import Const

class Piece(Slideable):
    def __init__(self, board=None, pos=None, color=None, symbol="P"):
        self.symbol = symbol
        self.pos = pos
        self.color = color
        self.board = board
        self.move_type = Const.ALL_DIRECTION

    def __str__(self):
        return self.symbol
