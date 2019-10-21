from movement import Coordinate
from pieces.piece import Piece


class Knight(Piece):
    representation = "N"
    value = 3

    def __init__(self, color):
        super().__init__(color)
        self.representation = "N"
        self.value = 3

    def get_legal_moves(self):
        """Define Knight legal moves in the shape of L"""
        if not self.active:
            return

        # Determine legal coordinate destinations
        legal_moves = []

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

