from movement import Coordinate
from pieces.piece import Piece


class King(Piece):
    """The King represents a chess piece capable of any movement of length one that the team depends on."""
    representation = "K"
    value = 25

    def __init__(self, color):
        super().__init__(color)

    def get_legal_moves(self):
        """Define King legal moves. Move one tile in any direction"""
        if not self.active:
            return

        # Determine legal coordinate destinations
        legal_moves = []
        for i in range (self.position.x -1, self.position.x + 2):
            for j in range(self.position.y - 1, self.position.y + 2):
                destination = Coordinate (i, j)
                if destination != self.position and King.is_valid_move(destination):
                    legal_moves.append(destination)  # Moves towards ally units will be pruned later

        return legal_moves
