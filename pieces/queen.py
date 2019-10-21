from typing import List

from movement import Coordinate
from pieces import Rook, Bishop


class Queen(Rook, Bishop):
    """The Queen represents a chess piece capable of diagonal, horizontal and vertical movement."""
    REPRESENTATION: str = "Q"
    VALUE: int = 9

    def __init__(self, color: bool) -> None:
        super().__init__(color)

    def get_legal_moves(self) -> List[Coordinate]:
        """Define Queen legal moves by combining the legal moves of a Rook and a Bishop in its position"""
        legal_moves: List[Coordinate] = []
        if not self.active:
            return legal_moves
        # Determine legal coordinate destinations
        legal_moves = Rook.get_legal_moves(self) + Bishop.get_legal_moves(self)
        return legal_moves

