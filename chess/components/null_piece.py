from .singleton import Singleton
from .piece import Piece


class NullPiece(Piece, metaclass=Singleton):
    def __init__(self, pos, sym):
        Piece.__init__(self, pos, sym) #Tempting to use super, but only do so if you know how it all works

    
    

    
