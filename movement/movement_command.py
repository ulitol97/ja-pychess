from board import board


class MovementCommand:
    def __init__(self, piece, origin, destination):
        self.piece = piece  # Piece affected by the movement
        self.hasMovedValue = self.piece.has_moved
        self.origin = origin  # Original coordinates of the movement
        self.destination = destination  # Destination coordinates of the movement
        self.destinationPiece = board.Board.get_piece(self.destination)

    def execute(self):
        if self.destinationPiece is not None:
            self.destinationPiece.active = False  # Kill the piece in the destination
        board.Board.tiles[self.destination.x][self.destination.y].piece = self.piece
        board.Board.tiles[self.origin.x][self.origin.y].piece = None
        self.piece.position = self.destination
        self.piece.has_moved = True

    def undo(self):
        board.Board.tiles[self.origin.x][self.origin.y].piece = self.piece
        self.piece.position = self.origin
        self.piece.has_moved = self.hasMovedValue
        board.Board.tiles[self.destination.x][self.destination.y].piece = self.destinationPiece
        if self.destinationPiece is not None:
            self.destinationPiece.active = True  # Revive the piece in the destination

