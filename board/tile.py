import pieces
from movement import Coordinate


class Tile:

    def __init__(self, x=None, y=None, piece=pieces.Piece()):
        self.position = Coordinate(x, y)
        self.piece = piece

    def __str__(self):
        return self.piece.__str__()

