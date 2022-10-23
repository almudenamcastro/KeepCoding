from settings import *


class LBoard:
    def __init__(self):
#    """crea un tablero. "-" es vacío, x es jugador 1. o es jugador 2"""
        self._column = ["-"] * BOARD_SIZE

    def __str__(self):
        return f"{self._column}"

    def add(self, char):
        if self._column[-1] != "-":
            return "the column is filled"
        i = self._column.index("-") 
        self._column [i] = char

class Board:
    def __init__(self):
        """crea un tablero. "-" es vacío, x es jugador 1. o es jugador 2"""
        self._board = [LBoard()] * BOARD_SIZE

    def __str__(self):
    #    return f"{[self._board[i]._column for i in range(BOARD_SIZE)]}"
        string = ""
        for i in range(BOARD_SIZE):
            string += f"{self._board[i]._column}\n"
        return string

#    def add(self, char, column):
 #       self._board[column].add(char)
  #      print(self._board)

columna=LBoard()
print(columna)
columna.add("x")
print(columna)

tablero = Board()
print(tablero)
print(tablero._board[3])
tablero._board[3].add("x")
print(tablero)