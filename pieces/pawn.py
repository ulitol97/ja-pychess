from typing import List

from board import board
from movement import Coordinate
from pieces.piece import Piece


class Pawn(Piece):
    """The Pawn represents a chess piece capable of forward movement and attacking other pieces diagonally."""
    REPRESENTATION: str = "P"
    VALUE: int = 1

    def __init__(self, color: bool) -> None:
        super().__init__(color)

    def get_legal_moves(self) -> List[Coordinate]:
        """Define Pawn legal moves. Move forward one tile or two in case it has not moved yet"""
        legal_moves: List[Coordinate] = []

        if not self.active:
            return legal_moves

        # Determine pawns moving direction
        mov_y: int
        if self.color == board.WHITE:
            mov_y = -1
        else:
            mov_y = 1

        # Determine legal coordinate destinations
        target_piece: Piece = board.Board.get_piece(self.position + Coordinate(mov_y, 0))
        if Pawn.is_valid_move(
                self.position + Coordinate(mov_y, 0)) and target_piece is None or target_piece.active is False:
            legal_moves.append(self.position + Coordinate(mov_y, 0))

        if not self.has_moved:
            target_piece = board.Board.get_piece(self.position + Coordinate(mov_y * 2, 0))
            if Pawn.is_valid_move(
                    self.position + Coordinate(mov_y * 2, 0)) and target_piece is None or target_piece.active is False:
                legal_moves.append(self.position + Coordinate(mov_y * 2, 0))

        # Determine legal coordinates if pawn can eat diagonally
        if Pawn.is_valid_move(self.position + Coordinate(mov_y, 1)):
            other_piece = board.Board.get_piece(self.position + Coordinate(mov_y, 1))
            if other_piece is not None and other_piece.active is True and other_piece.color != self.color:
                legal_moves.append(self.position + Coordinate(mov_y, 1))

        if Pawn.is_valid_move(self.position + Coordinate(mov_y, -1)):
            other_piece = board.Board.get_piece(self.position + Coordinate(mov_y, -1))
            if other_piece is not None and other_piece.active is True and other_piece.color != self.color:
                legal_moves.append(self.position + Coordinate(mov_y, -1))
        return legal_moves
