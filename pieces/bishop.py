from typing import List

import board
from movement import Coordinate
from pieces.piece import Piece


class Bishop(Piece):
    """The Bishop represents a chess piece capable of diagonal movement."""
    representation: str = "B"
    value: int = 3

    def __init__(self, color: bool) -> None:
        super().__init__(color)

    def get_legal_moves(self) -> List[Coordinate]:
        """Define Bishop legal moves. Move diagonally as much as desired"""
        legal_moves: List[Coordinate] = []

        if not self.active:
            return legal_moves

        # Determine legal coordinate destinations
        # UP RIGHT ----------------------------------------------

        i: int = self.position.x + 1
        j: int = self.position.y + 1

        # As long as there are no pieces in its path, allow move
        while i < board.Board.BOARD_SIZE and j < board.Board.BOARD_SIZE:
            piece: Piece = board.Board.get_piece(Coordinate(i, j))
            if piece is None:
                legal_moves.append(Coordinate(i, j))
                i += 1
                j += 1
            elif piece.color != self.color:
                legal_moves.append(Coordinate(i, j))
                break
            else:
                break

        # UP LEFT ----------------------------------------------

        i = self.position.x - 1
        j = self.position.y + 1

        # As long as there are no pieces in its path, allow move
        while i >= 0 and j < board.Board.BOARD_SIZE:
            piece: Piece = board.Board.get_piece(Coordinate(i, j))
            if piece is None:
                legal_moves.append(Coordinate(i, j))
                i -= 1
                j += 1
            elif piece.color != self.color:
                legal_moves.append(Coordinate(i, j))
                break
            else:
                break

        # DOWN RIGHT ----------------------------------------------

        i = self.position.x + 1
        j = self.position.y - 1

        # As long as there are no pieces in its path, allow move
        while i < board.Board.BOARD_SIZE and j >= 0:
            piece: Piece = board.Board.get_piece(Coordinate(i, j))
            if piece is None:
                legal_moves.append(Coordinate(i, j))
                i += 1
                j -= 1
            elif piece.color != self.color:
                legal_moves.append(Coordinate(i, j))
                break
            else:
                break

        # DOWN LEFT ----------------------------------------------

        i = self.position.x - 1
        j = self.position.y - 1

        # As long as there are no pieces in its path, allow move
        while i >= 0 and j >= 0:
            piece: Piece = board.Board.get_piece(Coordinate(i, j))
            if piece is None:
                legal_moves.append(Coordinate(i, j))
                i -= 1
                j -= 1
            elif piece.color != self.color:
                legal_moves.append(Coordinate(i, j))
                break
            else:
                break

        return legal_moves
