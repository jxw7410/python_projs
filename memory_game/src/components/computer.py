from .player import Player
from random import choice


class Computer(Player):
    def __init__(self):
        super().__init__('Computer')

    def get_move(self, *args):
        available_moves, known_moves, prev_card = args
        if prev_card and prev_card.value in known_moves:
            if len(known_moves[prev_card.value]) == 2:
                pos1, pos2 = known_moves[prev_card.value]
                return pos2 if prev_card.pos == pos1 else pos1

        return choice(list(available_moves))
