from settings import *
from utils import *
from linear_board import *

class Board:
    def __init__(self):
        """crea un tablero. "-" es vacío, x es jugador 1. o es jugador 2"""
        self._board = [LBoard() for i in range(BOARD_SIZE)]

    def __str__(self):
        string = "\n"
        #inicializo las filas de la última a la primera (quiero colocar los LBoards con el 0 abajo)
        for j in range(BOARD_SIZE-1, -1, -1):
            #voy de vector en vector (del 0 al 3) tomando el elemento que toca (elemento j)
            for i in range(BOARD_SIZE):
                string += f"| {self._board[i]._column[j]} "
            #al final de cada fila añado un salto de línea. 
            string += "|\n"
        string +="T"*17+"\n"
        return string

    def add(self, char, column):
        self._board[column].add(char)
        print(self)

    def victory(self, char):
        return self.victory_vert(char) or self.victory_hor(char) or self.victory_diag_up(char) or self.victory_diag_down(char)

    def victory_vert(self, char):
        for column in self._board:
            if column.victory(char):
                return True
        return False
    
    def victory_hor(self, char):
        pass
    
    def victory_diag_up(self, char):
        pass

    def victory_diag_down(self, char):
        pass

    def tie(self, char1, char2):
        return (self.victory(self, char1) == False) and (self.victory(self, char2) == False) and (self._column[-1] != "-")

columna = LBoard()
print(columna)
columna.add("o")

tablero = Board()
print(tablero)
tablero.add("x", 3)