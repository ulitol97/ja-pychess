from board import board
from pieces import Pawn
from colorama import Fore


class MovementCommand:
    def __init__(self, piece, origin, destination):
        self.piece = piece  # Piece affected by the movement
        self.hasMovedValue = self.piece.has_moved
        self.origin = origin  # Original coordinates of the movement
        self.destination = destination  # Destination coordinates of the movement
        self.destinationPiece = board.Board.get_piece(self.destination)
        self.originalClass = self.piece.__class__ # In order to recover from falls in trap tiles

    def execute(self):
        if self.destinationPiece is not None:
            self.destinationPiece.active = False  # Kill the piece in the destination
        board.Board.tiles[self.destination.x][self.destination.y].piece = self.piece
        board.Board.tiles[self.origin.x][self.origin.y].piece = None
        self.piece.position = self.destination
        self.piece.has_moved = True
        if board.Board.tiles[self.destination.x][self.destination.y].trap is True:
            print ("Fell into a "+ Fore.YELLOW + "trap" + Fore.RESET + "! Turned into a pawn")
            self.piece.__class__ = Pawn  # Falling into a trap causes change to pawn
            self.piece.representation = Pawn.representation

    def undo(self):
        board.Board.tiles[self.origin.x][self.origin.y].piece = self.piece
        self.piece.position = self.origin
        self.piece.has_moved = self.hasMovedValue
        board.Board.tiles[self.destination.x][self.destination.y].piece = self.destinationPiece
        if self.destinationPiece is not None:
            self.destinationPiece.active = True  # Revive the piece in the destination

        if board.Board.tiles[self.destination.x][self.destination.y].trap is True:
            self.piece.__class__ = self.originalClass  # Revert falling in trap
            self.piece.representation = self.originalClass.representation


