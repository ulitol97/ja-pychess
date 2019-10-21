from board import board
from pieces import Pawn, Queen
from colorama import Fore


class MovementCommand:
    def __init__(self, piece, origin, destination):
        self.piece = piece  # Piece affected by the movement
        self.hasMovedValue = self.piece.has_moved
        self.origin = origin  # Original coordinates of the movement
        self.destination = destination  # Destination coordinates of the movement
        self.destinationPiece = board.Board.get_piece(self.destination)
        self.originalClass = self.piece.__class__  # In order to recover from falls in trap tiles

    def execute(self):
        if self.destinationPiece is not None:
            self.destinationPiece.active = False  # Kill the piece in the destination
        board.Board.tiles[self.destination.x][self.destination.y].piece = self.piece
        board.Board.tiles[self.origin.x][self.origin.y].piece = None
        self.piece.position = self.destination
        self.piece.has_moved = True
        self.check_for_traps()
        self.check_for_pawn_promotion()

    def undo(self):
        board.Board.tiles[self.origin.x][self.origin.y].piece = self.piece
        self.piece.position = self.origin
        self.piece.has_moved = self.hasMovedValue
        board.Board.tiles[self.destination.x][self.destination.y].piece = self.destinationPiece
        if self.destinationPiece is not None:
            self.destinationPiece.active = True  # Revive the piece in the destination
        self.check_for_traps(True)
        self.check_for_pawn_promotion(True)

    def check_for_traps(self, undo=False):
        if board.Board.tiles[self.destination.x][self.destination.y].trap is True:
            if undo is True:
                self.piece.__class__ = self.originalClass  # Revert falling in trap
                self.piece.representation = self.originalClass.representation
            else:
                print (Fore.YELLOW + self.piece.__class__.__name__ + " fell into a trap: demoted to a Pawn" + Fore.RESET)
                self.piece.__class__ = Pawn  # Falling into a trap causes change to pawn
                self.piece.representation = Pawn.representation

    def check_for_pawn_promotion(self, undo=False):
        """Promote pawns to queen when reaching the end of the enemy field"""
        if isinstance(self.piece, Pawn):
            if (self.piece.color == board.WHITE and self.destination.x == 0) or (
                    self.piece.color == board.BLACK and self.destination.x == board.Board.BOARD_SIZE - 1):
                if undo is True:
                    self.piece.__class__ = Pawn  # Falling into a trap causes change to pawn
                    self.piece.representation = Pawn.representation
                else:
                    print(Fore.YELLOW + "Congrats, your Pawn was promoted to Queen" + Fore.RESET)
                    self.piece.__class__ = Queen  # Falling into a trap causes change to pawn
                    self.piece.representation = Queen.representation
