from abc import ABC
from board import board
from movement import Coordinate
from colorama import Fore


class Piece(ABC):
    """The Piece class is an abstract class serving as a template for all the chess pieces."""
    representation = "X"
    value = 0

    def __init__(self, color=None, x=None, y=None):
        """Initialize the chess piece with a given position and color"""
        self.position = Coordinate(x, y)
        self.has_moved = False
        self.active = True
        self.color = color
        if color is None:
            self.color = board.WHITE

    def __str__(self):
        """Return a letter representing the piece colored to represent its side"""
        if self.color == board.WHITE:
            return Fore.BLUE + self.representation + Fore.RESET
        elif self.color == board.BLACK:
            return Fore.RED + self.representation + Fore.RESET
        else:
            return self.representation

    def get_legal_moves(self):
        """Return a list of all the movements the piece can do without leaving the board"""
        if not self.active:
            return

        # Determine legal coordinate destinations
        legal_moves = []
        return legal_moves

    @staticmethod
    def is_valid_move(coordinate):
        """Check if a given coordinate is locate inside of the game board"""
        if coordinate.x >= board.Board.BOARD_SIZE or coordinate.y >= board.Board.BOARD_SIZE:
            return False
        if coordinate.x < 0 or coordinate.y < 0:
            return False

        return True
