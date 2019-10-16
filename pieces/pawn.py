from board import board
from movement import Coordinate
from pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.representation = "P"
        self.value = 1

    def get_legal_moves(self):
        """Define Pawn legal moves. Move forward one tile or two in case it has not moved yet"""
        if not self.active:
            return

        # Determine pawns moving direction
        if self.color == board.WHITE:
            mov_y = -1
        else:
            mov_y = 1

        # Determine legal coordinate destinations
        legal_moves = []
        if Pawn.is_valid_move(self.position + Coordinate(0, mov_y)):
            legal_moves.append(self.position + Coordinate(0, mov_y))
        if not self.has_moved:
            if Pawn.is_valid_move(self.position + Coordinate(0, mov_y*2)):
                legal_moves.append(self.position + Coordinate(0, mov_y*2))

        return legal_moves

