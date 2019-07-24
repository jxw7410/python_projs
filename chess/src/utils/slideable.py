from abc import ABC
from .constants import Const


class Slideable(ABC):
    def __init__(self):
        super().__init__()

    def moves(self):
        if self.move_type == Const.ORTHAGONAL:
            return self.generate_move_sets(self.orthagonal_delta)
        elif self.move_type == Const.DIAGONAL:
            return self.generate_move_sets(self.diagonal_delta)
        elif self.move_type == Const.ALL_DIRECTION:
            return self.generate_move_sets(self.orthagonal_delta) + self.generate_move_sets(self.diagonal_delta)

    
    def generate_move_sets(self, deltas):
        def get_delta(pos, delta):
            px, py = pos
            if 0 > px or 0 > py or px == Const.BOARD_SIZE or py == Const.BOARD_SIZE or self.board[px, py].color == self.color:        
                return []
            elif self.board[px, py].color and self.board[px, py].color != self.color:
                return [pos]
            else:
                dx, dy = delta 
                return [pos] + get_delta([px + dx, py + dy], delta)
        
        res = []
        for delta in deltas:
            res += get_delta([self.pos[0] + delta[0], self.pos[1] + delta[1]], delta)

        return res


    @property
    def orthagonal_delta(self):
        return [
            (1, 0),
            (-1, 0),
            (0,  1),
            (0, -1)
        ]

    @property
    def diagonal_delta(self):
        return [
            (1,  1),
            (-1, -1),
            (1, -1),
            (-1,  1),
        ]
