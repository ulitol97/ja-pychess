class Tile:
    """The Tile class represents a tile of the game board. A tile may be occupied by a piece and
     maybe a trap tile that will demoted its piece to a Pawn"""
    def __init__(self, piece=None, trap=False):
        """Initiate the tile with a piece and a trap or not"""
        self.piece = piece
        self.trap = trap

    def __str__(self):
        """Return the string representation of the data inside the Tile"""
        if self.piece is None:
            return " "
        else:
            return self.piece.__str__()

