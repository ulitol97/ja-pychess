from pieces.piece import Piece


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.value = 3

    def __str__(self):
        return "N"
