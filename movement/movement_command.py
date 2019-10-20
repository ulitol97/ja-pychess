class MovementCommand:
    def __init__(self, piece, origin, destination):
        self.piece = piece  # Piece affected by the movement
        self.origin = origin  # Original coordinates of the movement
        self.destination = destination  # Destination coordinates of the movement

    def execute(self):
        self.piece.position = self.destination

    def undo (self):
        self.piece.position = self.origin

