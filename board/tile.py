class Tile:

    def __init__(self, piece=None):
        self.piece = piece

    def __str__(self):
        if self.piece is None:
            return " "
        else:
            return self.piece.__str__()

