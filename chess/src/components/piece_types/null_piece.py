from src.utils.singleton import Singleton
from src.components.piece import Piece


class NullPiece(Piece):
    __metaclass__ = Singleton
    def __init__(self, pos, sym):
        Piece.__init__(self, pos=pos, symbol=sym)
       

    
    

    
