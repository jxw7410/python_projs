from .consts import BOARD_SIZE
from .piece import Piece

class Board:
    def __init__(self):
        self.__grid = [[" "] * BOARD_SIZE() for i in range(BOARD_SIZE())]

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

    #Public Methods
    def initialize(self):
        self.__grid[0] = [Piece(board, ), Piece(), Piece(),
                          Piece(), Piece(), Piece(), 
                          Piece(), Piece()]
        
        self.__grid[7] = [Piece(), Piece(), Piece(),
                          Piece(), Piece(), Piece(),
                          Piece(), Piece()]

        for c_idx in range(BOARD_SIZE()):
            self[1, c_idx], self[6, c_idx] = None, None 
        


    def move_piece(start_pos, end_pos):
        self[start_pos], self[end_pos] = self[end_pos], self[start_pos]
    



    
