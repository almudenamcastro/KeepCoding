import pytest
from linear_board import *
from settings import *

def test_empty_board(): 
    b = LBoard()
    assert b != None
    assert b.victory("x") == False
    assert b.victory("o") == False

def test_add():
    b = LBoard()
    for i in range(BOARD_SIZE):
        b.add("x")
    assert b.victory("x") == True
    assert b._column[-1] == "x"

def test_victory():
    b = LBoard()
    for i in range(WIN_STRIKE):
        b.add("x")
    assert b.victory("x") == True
