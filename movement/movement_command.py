from board import board
from movement import Coordinate
from pieces import Pawn, Queen, Piece
from colorama import Fore


class MovementCommand:
    """
    The MovementCommand class represents an action in which a piece is moved form ine tile to another, triggering
    the logic consequences of the movement regarding the movement origin and destination.
    It does not check if the movement is legal, it should be checked beforehand.
    It is part of the Execution pattern and allows to:
        -> Execute movements
        -> Undo movements
    """
    def __init__(self, piece: Piece, origin: Coordinate, destination: Coordinate):
        """Initialize a movement command and store the necessary data to be able to undo it later"""
        self.piece: Piece = piece  # Piece affected by the movement
        self.hasMovedValue: bool = self.piece.has_moved
        self.origin: Coordinate = origin  # Original coordinates of the movement
        self.destination: Coordinate = destination  # Destination coordinates of the movement
        self.destinationPiece: Piece = board.Board.get_piece(self.destination)
        self.originalClass = self.piece.__class__  # In order to recover from falls in trap tiles

    def execute(self):
        """Execute the movement specified in the command"""
        if self.destinationPiece is not None:
            self.destinationPiece.active = False  # Kill the piece in the destination
        board.Board.tiles[self.destination.x][self.destination.y].piece = self.piece
        board.Board.tiles[self.origin.x][self.origin.y].piece = None
        self.piece.position = self.destination
        self.piece.has_moved = True
        self.check_for_traps()
        self.check_for_pawn_promotion()

    def undo(self):
        """Undo the movement specified in the command, taking for granted it was executed before"""
        board.Board.tiles[self.origin.x][self.origin.y].piece = self.piece
        self.piece.position = self.origin
        self.piece.has_moved = self.hasMovedValue
        board.Board.tiles[self.destination.x][self.destination.y].piece = self.destinationPiece
        if self.destinationPiece is not None:
            self.destinationPiece.active = True  # Revive the piece in the destination
        self.check_for_traps(True)
        self.check_for_pawn_promotion(True)

    def check_for_traps(self, undo:bool = False):
        """Check if the movement destination is a trap tile and activate it if it is"""
        if board.Board.tiles[self.destination.x][self.destination.y].trap is True:
            if undo is True:
                self.piece.__class__ = self.originalClass  # Revert falling in trap
                self.piece.REPRESENTATION = self.originalClass.REPRESENTATION
            else:
                print (Fore.YELLOW + self.piece.__class__.__name__ + " fell into a trap: demoted to a Pawn" + Fore.RESET)
                self.piece.__class__ = Pawn  # Falling into a trap causes change to pawn
                self.piece.REPRESENTATION = Pawn.REPRESENTATION

    def check_for_pawn_promotion(self, undo: bool = False):
        """Promote pawns to queen when reaching the end of the enemy field"""
        if isinstance(self.piece, Pawn):
            if (self.piece.color == board.WHITE and self.destination.x == 0) or (
                    self.piece.color == board.BLACK and self.destination.x == board.Board.BOARD_SIZE - 1):
                if undo is True:
                    self.piece.__class__ = Pawn  # Falling into a trap causes change to pawn
                    self.piece.REPRESENTATION = Pawn.REPRESENTATION
                else:
                    print(Fore.YELLOW + "Congrats, your Pawn was promoted to Queen" + Fore.RESET)
                    self.piece.__class__ = Queen  # Falling into a trap causes change to pawn
                    self.piece.REPRESENTATION = Queen.REPRESENTATION
