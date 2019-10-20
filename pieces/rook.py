from board import board
from movement import Coordinate
from pieces.piece import Piece


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.representation = "R"
        self.value = 5

    def get_legal_moves(self):
        """Define Rook legal moves. Move horizontally or vertically as much as desired"""
        if not self.active:
            return

        # Determine legal coordinate destinations
        legal_moves = []

        # Get movement limits regarding the position of other pieces on the board
        max_x = self.position.x
        min_x = self.position.x
        max_y = self.position.y
        min_y = self.position.y

        # Getting maximum movement in X axis
        for i in range (self.position.x+1, board.Board.BOARD_SIZE):
            if board.Board.get_piece(Coordinate(i, self.position.y)) is not None:
                max_x = i-1
                break

        # Getting minimum movement in X axis
        for i in range(self.position.x - 1, - 1, -1):
            if board.Board.get_piece(Coordinate(i, self.position.y)) is not None:
                min_x = i+1
                break

        # Getting maximum movement in Y axis
        for j in range(self.position.y + 1, board.Board.BOARD_SIZE):
            if board.Board.get_piece(Coordinate(self.position.x, j)) is not None:
                max_y = j-1
                break

        # Getting minimum movement in Y axis
        for j in range(self.position.y - 1, - 1, -1):
            if board.Board.get_piece(Coordinate(self.position.x, j)) is not None:
                min_y = j+1
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
