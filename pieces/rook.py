from typing import List

from board import board
from movement import Coordinate
from pieces.piece import Piece


class Rook(Piece):
    """The Rook represents a chess piece capable of horizontal and vertical movement."""
    representation = "R"
    value: int = 5

    def __init__(self, color: bool) -> None:
        super().__init__(color)

    def get_legal_moves(self) -> List[Coordinate]:
        """Define Rook legal moves. Move horizontally or vertically as much as desired"""
        legal_moves: List[Coordinate] = []

        if not self.active:
            return legal_moves

        # Determine legal coordinate destinations
        # Get movement limits regarding the position of other pieces on the board
        max_x: int = board.Board.BOARD_SIZE-1
        min_x: int = 0
        max_y: int = board.Board.BOARD_SIZE-1
        min_y: int = 0

        # Getting maximum movement in X axis
        for i in range (self.position.x+1, board.Board.BOARD_SIZE):
            piece: Piece = board.Board.get_piece(Coordinate(i, self.position.y))
            if piece is not None and piece.active is True:
                if piece.color == self.color:
                    max_x = i-1
                else:
                    max_x = i
                break

        # Getting minimum movement in X axis
        for i in range(self.position.x - 1, - 1, -1):
            piece = board.Board.get_piece(Coordinate(i, self.position.y))
            if piece is not None and piece.active is True:
                if piece.color == self.color:
                    min_x = i+1
                else:
                    min_x = i
                break

        # Getting maximum movement in Y axis
        for j in range(self.position.y + 1, board.Board.BOARD_SIZE):
            piece = board.Board.get_piece(Coordinate(self.position.x, j))
            if piece is not None and piece.active is True:
                if piece.color == self.color:
                    max_y = j-1
                else:
                    max_y = j
                break

        # Getting minimum movement in Y axis
        for j in range(self.position.y - 1, - 1, -1):
            piece = board.Board.get_piece(Coordinate(self.position.x, j))
            if piece is not None and piece.active is True:
                if piece.color == self.color:
                    min_y = j+1
                else:
                    min_y = j
                break

        # Possible moves in the X axis
        for i in range (min_x, max_x + 1):
            if i != self.position.x:
                legal_moves.append(Coordinate(i, self.position.y))

        # Possible moves in the Y axis
        for j in range(min_y, max_y + 1):
            if j != self.position.y:
                legal_moves.append(Coordinate(self.position.x, j))

        return legal_moves
