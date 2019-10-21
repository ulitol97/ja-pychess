from typing import List

from movement import Coordinate
from pieces.piece import Piece


class Knight(Piece):
    """The Knight represents a chess piece capable of L shaped movement."""
    representation: str = "N"
    value: int = 3

    def __init__(self, color: bool) -> None:
        super().__init__(color)

    def get_legal_moves(self) -> List[Coordinate]:
        """Define Knight legal moves in the shape of L"""
        legal_moves: List[Coordinate] = []

        if not self.active:
            return legal_moves

        # Determine legal coordinate destinations
        if Knight.is_valid_move(Coordinate(self.position.x + 1, self.position.y + 2)):
            legal_moves.append(Coordinate(self.position.x + 1, self.position.y + 2))

        if Knight.is_valid_move(Coordinate(self.position.x + 2, self.position.y + 1)):
            legal_moves.append(Coordinate(self.position.x + 2, self.position.y + 1))

        if Knight.is_valid_move(Coordinate(self.position.x + 2, self.position.y - 1)):
            legal_moves.append(Coordinate(self.position.x + 2, self.position.y - 1))

        if Knight.is_valid_move(Coordinate(self.position.x + 1, self.position.y - 2)):
            legal_moves.append(Coordinate(self.position.x + 1, self.position.y - 2))

        if Knight.is_valid_move(Coordinate(self.position.x - 1, self.position.y - 2)):
            legal_moves.append(Coordinate(self.position.x - 1, self.position.y - 2))

        if Knight.is_valid_move(Coordinate(self.position.x - 2, self.position.y - 1)):
            legal_moves.append(Coordinate(self.position.x - 2, self.position.y - 1))

        if Knight.is_valid_move(Coordinate(self.position.x - 2, self.position.y + 1)):
            legal_moves.append(Coordinate(self.position.x - 2, self.position.y + 1))

        if Knight.is_valid_move(Coordinate(self.position.x - 1, self.position.y + 2)):
            legal_moves.append(Coordinate(self.position.x - 1, self.position.y + 2))

        return legal_moves

