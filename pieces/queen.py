from pieces import Rook, Bishop


class Queen(Rook, Bishop):
    def __init__(self, color):
        super().__init__(color)
        self.representation = "Q"
        self.value = 9

    def get_legal_moves(self):
        """Define Queen legal moves by combining the legal moves of a Rook and a Bishop in its position"""
        if not self.active:
            return
        # Determine legal coordinate destinations
        legal_moves = Rook.get_legal_moves(self) + Bishop.get_legal_moves(self)
        return legal_moves

