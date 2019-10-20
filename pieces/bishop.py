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
        while board.Board.get_piece(
                Coordinate(i, j)) is None and i < board.Board.BOARD_SIZE and j < board.Board.BOARD_SIZE:
            legal_moves.append(Coordinate(i, j))
            i += 1
            j += 1

        #  Allow move if the tile is occupied by enemy
        if Bishop.is_valid_move(Coordinate(i, j)) and board.Board.get_piece(Coordinate(i, j)).color != self.color:
            legal_moves.append(Coordinate(i, j))

        # UP LEFT ----------------------------------------------

        i = self.position.x - 1
        j = self.position.y + 1

        # As long as there are no pieces in its path, allow move
        while board.Board.get_piece(Coordinate(i, j)) is None and i >= 0 and j < board.Board.BOARD_SIZE:
            legal_moves.append(Coordinate(i, j))
            i -= 1
            j += 1

        #  Allow move if the tile is occupied by enemy
        if Bishop.is_valid_move(Coordinate(i, j)) and board.Board.get_piece(Coordinate(i, j)).color != self.color:
            legal_moves.append(Coordinate(i, j))

        # DOWN RIGHT ----------------------------------------------

        i = self.position.x + 1
        j = self.position.y - 1

        # As long as there are no pieces in its path, allow move
        while board.Board.get_piece(
                Coordinate(i, j)) is None and i < board.Board.BOARD_SIZE and j >= 0:
            legal_moves.append(Coordinate(i, j))
            i += 1
            j -= 1

        #  Allow move if the tile is occupied by enemy
        if Bishop.is_valid_move(Coordinate(i, j)) and board.Board.get_piece(Coordinate(i, j)).color != self.color:
            legal_moves.append(Coordinate(i, j))

        # DOWN LEFT ----------------------------------------------

        i = self.position.x - 1
        j = self.position.y - 1

        # As long as there are no pieces in its path, allow move
        while board.Board.get_piece(
                Coordinate(i, j)) is None and i >= 0 and j >= 0:
            legal_moves.append(Coordinate(i, j))
            i -= 1
            j -= 1

        #  Allow move if the tile is occupied by enemy
        if Bishop.is_valid_move(Coordinate(i, j)) and board.Board.get_piece(Coordinate(i, j)).color != self.color:
            legal_moves.append(Coordinate(i, j))

        return legal_moves
