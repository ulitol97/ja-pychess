from abc import ABC, abstractmethod
from board import board
from movement import Coordinate
from colorama import Fore


class Piece(ABC):
    def __init__(self, color=None, x=None, y=None):
        self.position = Coordinate(x, y)
        self.has_moved = False
        self.value = 0
        self.representation = "X"
        if color is None:
            self.color = board.WHITE

    def __str__(self):
        if self.color == board.WHITE:
            return Fore.BLUE + self.representation + Fore.RESET
        elif self.color == board.BLACK:
            return Fore.RED + self.representation + Fore.RESET
        else:
            return self.representation

    def is_valid_move (self, coordinate):
        if coordinate.x >= board.Board.BOARD_SIZE or coordinate.y >= board.Board.BOARD_SIZE or coordinate.x < 0 or coordinate.y < 0:
            return False
        elif ...