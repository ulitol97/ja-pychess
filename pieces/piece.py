from abc import ABC, abstractmethod
from board import board
from colorama import Fore


class Piece(ABC):
    def __init__(self, color=None):
        self.representation = "X"
        self.value = 0
        if color is None:
            color = board.WHITE
        self.color = color

    def __str__(self):
        if self.color == board.WHITE:
            return Fore.BLUE + self.representation + Fore.RESET
        elif self.color == board.BLACK:
            return Fore.RED + self.representation + Fore.RESET
        else:
            return self.representation
