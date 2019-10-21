class Tile:

    def __init__(self, piece=None, trap=False):
        self.piece = piece
        self.trap = trap

    def __str__(self):
        if self.piece is None:
            return " "
        else:
            return self.piece.__str__()

