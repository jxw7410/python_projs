

class Piece():
    def __init__(self, board,  pos, symbol="P"):
        self.symbol = symbol
        self.pos = pos
        self.moves = []
        self.board = board

    def __str__(self):
        return self.symbol
    

    

    