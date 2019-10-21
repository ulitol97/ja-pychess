from typing import List

from movement import Coordinate
from pieces.piece import Piece


class King(Piece):
    """The King represents a chess piece capable of any movement of length one that the team depends on."""
    REPRESENTATION: str = "K"
    VALUE: int = 25

    def __init__(self, color: bool) -> None:
        super().__init__(color)

    def get_legal_moves(self) -> List[Coordinate]:
        """Define King legal moves. Move one tile in any direction"""
        legal_moves: List[Coordinate] = []

        if not self.active:
            return legal_moves

        # Determine legal coordinate destinations
        for i in range (self.position.x - 1, self.position.x + 2):
            for j in range(self.position.y - 1, self.position.y + 2):
                destination: Coordinate = Coordinate (i, j)
                if destination != self.position and King.is_valid_move(destination):
                    legal_moves.append(destination)  # Moves towards ally units will be pruned later

        return legal_moves
