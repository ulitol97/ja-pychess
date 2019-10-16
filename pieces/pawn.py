from pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.value = 1

    def __str__(self):
        return "P"
