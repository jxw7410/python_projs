import re as regex
from .player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    
    def get_move(self, *args):
        user_input = input('Please input a coordinate, for ex: 1, 3 etc:\n')
        return self.__parse_input(user_input)
        
    def delay(self):
        pass 
        
    def __parse_input(self, input):
        num_array = regex.findall(r'\d+', input.replace(',', " "))

        if len(num_array) != 2:
            raise ValueError("Input contains less or more than 2 numbers")

        return map(lambda arg: int(arg), num_array)
