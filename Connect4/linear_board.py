from settings import *
from utils import *

class LBoard:
    def __init__(self):
#    """crea un tablero. "-" es vacío, x es jugador 1. o es jugador 2"""
        self._column = ["-"] * BOARD_SIZE

    def __str__(self):
        return f"{self._column}"

    def __repr__(self):
        return self.__str__()

    def add(self, char):
        if self._column[-1] != "-":
            return "the column is full"
        i = self._column.index("-") 
        self._column [i] = char
        print(self)
    
    def victory(self, char):
        return find_streak(self._column, char, WIN_STRIKE)

    def tie(self, char1, char2):
        return (self.victory(self, char1) == False) and (self.victory(self, char2) == False) and (self._column[-1] != "-")