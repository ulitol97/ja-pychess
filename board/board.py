import string
from board.tile import Tile
import pieces
from colorama import Back

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
                row.append(Tile())
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
        white_pieces = [pieces.Rook(WHITE), pieces.Knight(WHITE), pieces.Bishop(WHITE), pieces.Queen(WHITE),
                        pieces.King(WHITE), pieces.Bishop(WHITE), pieces.Knight(WHITE), pieces.Rook(WHITE)]

        # Add special pieces
        for i in range (len(self.tiles[self.BOARD_SIZE-1])):
            self.tiles[self.BOARD_SIZE - 1][i].piece = white_pieces[i]
            self.tiles[0][i].piece = black_pieces[i]

        # Lines of pawns
        for j in range (self.BOARD_SIZE):
            self.tiles[self.BOARD_SIZE-2][j].piece = pieces.Pawn(WHITE)
            self.tiles[1][j].piece = pieces.Pawn(BLACK)

    def __str__(self):
        """Returns a human readable representation of the chess board"""
        column_letters = "  "
        board = ""
        for i in range (self.BOARD_SIZE):
            column_letters += " {} ".format(string.ascii_lowercase[i])
            row_number = str(self.BOARD_SIZE-i)
            board += row_number + "  "
            for j in range (self.BOARD_SIZE):
                if i % 2 != 0 and j % 2 == 0 or i % 2 == 0 and j % 2 != 0:
                    board += Back.LIGHTBLACK_EX
                else:
                    board += Back.LIGHTWHITE_EX
                board += " {} ".format(self.tiles[i][j])
                board += Back.RESET
            board += ("  " + row_number + "\n")

        return column_letters + "\n" + board + column_letters


