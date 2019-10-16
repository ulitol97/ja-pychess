from pieces.piece import Piece


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.representation = "N"
        self.value = 3

