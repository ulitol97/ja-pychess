import string
from board.tile import Tile

# Program constants for each side of the board
WHITE = True
BLACK = False


class Board:
    BOARD_SIZE = 8

    def __init__(self, player_side=WHITE):
        self.tiles = self.init_board()
        self.player_side = player_side
        self.cpu_side = not player_side

    def init_board(self):
        """Initializes the matrix containing all the board tiles"""
        tiles = []
        for i in range(self.BOARD_SIZE):
            row = []
            for j in range (self.BOARD_SIZE):
                row.append(Tile(i, j))
            tiles.append(row)
        return tiles

    def __str__(self):
        """Returns a human readable representation of the chess board"""
        column_letters = "\t"
        board = ""
        for i in range (self.BOARD_SIZE):
            column_letters += " {} ".format(string.ascii_lowercase[i])
            row_number = str(self.BOARD_SIZE-i)
            board += row_number + "\t"
            for j in range (self.BOARD_SIZE):
                board += " {} ".format(self.tiles[i][j].piece)
            board += ("\t" + row_number + "\n")

        return column_letters + "\n" + board + column_letters


