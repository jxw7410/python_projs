from .piece import Piece
from .utils import Constants



class Board:
    def __init__(self):
        self.__grid = [ [" "] * Constants.BOARD_SIZE for i in range(Constants.BOARD_SIZE)]

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
        self.__grid[0] = [Piece(self, (0, 0)), Piece(self, (0, 1)), Piece(self,(0, 2)),
                          Piece(self, (0, 3)), Piece(self, (0, 4)), Piece(self,(0, 5)), 
                          Piece(self, (0, 6)), Piece(self, (0, 7))]
        
        self.__grid[7] = [Piece(self, (7, 0)), Piece(self, (7, 1)), Piece(self, (7, 2)),
                          Piece(self, (7, 3)), Piece(self, (7, 4)), Piece(self, (7, 5)),
                          Piece(self, (7, 6)), Piece(self, (7, 7))]

        for c_idx in range(Constants.BOARD_SIZE):
            self[1, c_idx], self[6, c_idx] = None, None 
        


    def move_piece(start_pos, end_pos):
        self[start_pos], self[end_pos] = self[end_pos], self[start_pos]
    



    
