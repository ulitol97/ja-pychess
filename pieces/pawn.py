from pieces.piece import Piece


class Pawn(Piece):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "P"
