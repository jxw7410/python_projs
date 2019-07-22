import re as regex
import time
from .utils.util import clear
from .utils.errors import AlreadyPlacedError
from .components.board import Board
from .components.human import Human
from .components.computer import Computer
from collections import defaultdict

class Game:
    def __init__(self, player_name, board_size):
        self.board_size = board_size
        self.board = Board(board_size)
        self.player = Human(player_name)
        self.computer = Computer()
        self.current_player = self.player
        self.available_moves = set()
        self.known_moves = defaultdict(lambda: [])
        self.is_over = False
        self.previous_card = None

    # Public Methods
    def start(self):
        self.board.populate()
        self.__build_moves()
        while not self.is_over:
            self.play()
            if self.board.won():
                self.is_over = True


    def play(self):
        self.__render()
        self.current_player.delay()
        try:
            x, y = self.current_player.get_move(self.available_moves, self.known_moves, self.previous_card)
        except Exception as error:
            print(error)
            input('Press any key to continue...\n')
        else:
            if self.board.valid_coord(x, y):
                try:
                    self.process_board(x, y)
                except Exception as error:
                    print(error)
                    input('Press any key to continue...\n')
            else:
                print('Coordinate input exceed bounds of Board.')
                input('Press any key to continue...\n')

    def process_board(self, x, y):
        if self.board[x, y].is_reveal:
            raise AlreadyPlacedError('The coordinates are already in used.')

        self.board[x, y].reveal()
        val = self.board[x,y].value

        if val in self.known_moves:
            if (x, y) not in self.known_moves[val]:
                self.known_moves[self.board[x, y].value].append(
                    self.board[x, y].pos)
        else:
            self.known_moves[self.board[x, y].value].append(self.board[x, y].pos)

        if not self.previous_card:
            self.previous_card = self.board[x, y]
            self.available_moves.remove((x,y))

        elif self.previous_card.value != self.board[x, y].value:
            self.__no_match(x, y)

        else:
            self.current_player.update_points()
            self.available_moves.remove((x,y))
            self.previous_card = None

       

    # Private Methods
    def __swap_players(self):
        self.current_player = self.player if self.current_player == self.computer else self.computer

    def __render(self):
        clear()
        print(self.current_player)
        self.board.render()
    
    def __no_match(self, x, y):
        self.__render()
        print('There is no Match\n')
        self.previous_card.hide()
        self.board[x, y].hide()
        self.available_moves.add((x, y))
        self.previous_card = None
        self.__swap_players()
        time.sleep(1)
       

    def __build_moves(self):
        for r_idx in range(self.board_size):
            for c_idx in range(self.board_size):
                self.available_moves.add((r_idx, c_idx))
