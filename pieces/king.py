from pieces.piece import Piece


class King(Piece):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "K"
