from abc import ABC
from typing import List

from board import board
from movement import Coordinate
from colorama import Fore


class Piece(ABC):
    """The Piece class is an abstract class serving as a template for all the chess pieces."""
    representation: str = "X"  # Letter representing the piece
    value: int = 0  # "Value" of the piece for future AI bases on a heusristc

    def __init__(self, color: bool = None, x: int = None, y: int = None) -> None:
        """Initialize the chess piece with a given position and color"""
        self.position: Coordinate = Coordinate(x, y)
        self.has_moved: bool = False
        self.active: bool = True
        self.color: bool = color
        if color is None:
            self.color = board.WHITE

    def __str__(self) -> str:
        """Return a letter representing the piece colored to represent its side"""
        if self.color == board.WHITE:
            return Fore.BLUE + self.representation + Fore.RESET
        elif self.color == board.BLACK:
            return Fore.RED + self.representation + Fore.RESET
        else:
            return self.representation

    def get_legal_moves(self) -> List[Coordinate]:
        """Return a list of all the movements the piece can do without leaving the board"""
        # Determine legal coordinate destinations
        legal_moves: List[Coordinate] = []
        return legal_moves

    @staticmethod
    def is_valid_move(coordinate: Coordinate) -> bool:
        """Check if a given coordinate is locate inside of the game board"""
        if coordinate.x >= board.Board.BOARD_SIZE or coordinate.y >= board.Board.BOARD_SIZE:
            return False
        if coordinate.x < 0 or coordinate.y < 0:
            return False

        return True
