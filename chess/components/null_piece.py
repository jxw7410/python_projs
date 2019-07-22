from .singleton import Singleton
from .piece import Piece


class NullPiece(Piece, metaclass=Singleton):
    def __init__(self, pos, sym):
        super().__init__(pos, sym)
        
    


    
