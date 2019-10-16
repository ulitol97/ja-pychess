from abc import ABC, abstractmethod
from board import board


class Piece(ABC):
    def __init__(self, color=None):
        self.value = 0
        if color is None:
            color = board.WHITE
        self.color = color

    @abstractmethod
    def __str__(self):
        return "X"
