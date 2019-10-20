import board
from movement import Coordinate
from pieces.piece import Piece


class Bishop(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.representation = "B"
        self.value = 3

    def get_legal_moves(self):
        """Define Bishop legal moves. Move diagonally as much as desired"""
        if not self.active:
            return

        # Determine legal coordinate destinations
        legal_moves = []

        # UP RIGHT ----------------------------------------------

        i = self.position.x + 1
        j = self.position.y + 1

        # As long as there are no pieces in its path, allow move
        while i < board.Board.BOARD_SIZE and j < board.Board.BOARD_SIZE:
            piece = board.Board.get_piece(Coordinate(i, j))
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
            piece = board.Board.get_piece(Coordinate(i, j))
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
            piece = board.Board.get_piece(Coordinate(i, j))
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
            piece = board.Board.get_piece(Coordinate(i, j))
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
