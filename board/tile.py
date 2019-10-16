import pieces
from movement import Coordinate


class Tile:

    def __init__(self, x=None, y=None, piece=None):
        self.position = Coordinate(x, y)
        self.piece = piece

    def __str__(self):
        if self.piece is None:
            return "X"
        else:
            return self.piece.__str__()

