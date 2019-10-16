import string
from board.tile import Tile
import pieces

# Program constants for each side of the board
WHITE = True
BLACK = False


class Board:
    BOARD_SIZE = 8

    def __init__(self, player_side=WHITE):
        self.__init_board()
        self.player_side = player_side
        self.cpu_side = not player_side

    def __init_board(self):
        """Initializes the matrix containing all the board tiles"""
        tiles = []
        for i in range(self.BOARD_SIZE):
            row = []
            for j in range (self.BOARD_SIZE):
                row.append(Tile(i, j))
            tiles.append(row)

        self.tiles = tiles
        self.__place_pieces()
        return tiles

    def __place_pieces(self):
        """Places the contents od the chessboard """
        # Standard black pieces behind the line of pawns
        black_pieces = [pieces.Rook(BLACK), pieces.Knight(BLACK), pieces.Bishop(BLACK), pieces.Queen(BLACK),
                        pieces.King(BLACK), pieces.Bishop(BLACK), pieces.Knight(BLACK), pieces.Rook(BLACK)]

        # Standard white pieces behind the line of pawns
        white_pieces = black_pieces.copy()
        for piece in white_pieces:
            piece.color = WHITE
        # Add special pieces
        for i in range (len(self.tiles[self.BOARD_SIZE-1])):
            self.tiles[self.BOARD_SIZE - 1][i].piece = black_pieces[i]
            self.tiles[0][i].piece = white_pieces[i]

        # Lines of pawns
        for j in range (self.BOARD_SIZE):
            self.tiles[self.BOARD_SIZE-2][j].piece = pieces.Pawn(BLACK)
            self.tiles[1][j].piece = pieces.Pawn(WHITE)

    def __str__(self):
        """Returns a human readable representation of the chess board"""
        column_letters = "\t"
        board = ""
        for i in range (self.BOARD_SIZE):
            column_letters += " {} ".format(string.ascii_lowercase[i])
            row_number = str(self.BOARD_SIZE-i)
            board += row_number + "\t"
            for j in range (self.BOARD_SIZE):
                board += " {} ".format(self.tiles[i][j])
            board += ("\t" + row_number + "\n")

        return column_letters + "\n" + board + column_letters


