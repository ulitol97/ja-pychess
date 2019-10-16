from pieces.piece import Piece


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.representation = "R"
        self.value = 5

    def get_legal_moves(self):
        """Define Rook legal moves. Move horizontally or vertically as much as desired"""
        if not self.active:
            return

        # Determine pawns moving direction
        if self.color == board.WHITE:
            mov_y = -1
        else:
            mov_y = 1

        # Determine legal coordinate destinations
        legal_moves = []
        if Pawn.is_valid_move(self.position + Coordinate(0, mov_y)):
            legal_moves.append(self.position + Coordinate(0, mov_y))
        if not self.has_moved:
            if Pawn.is_valid_move(self.position + Coordinate(0, mov_y * 2)):
                legal_moves.append(self.position + Coordinate(0, mov_y * 2))

        return legal_moves
