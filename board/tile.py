from pieces import Piece


class Tile:
    """The Tile class represents a tile of the game board. A tile may be occupied by a piece and
     maybe a trap tile that will demoted its piece to a Pawn"""
    def __init__(self, piece: Piece = None, trap: bool = False) -> None:
        """Initiate the tile with a piece and a trap or not"""
        self.piece: Piece = piece
        self.trap: bool = trap

    def __str__(self) -> str:
        """Return the string representation of the data inside the Tile"""
        if self.piece is None:
            return " "
        else:
            return self.piece.__str__()

