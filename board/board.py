import string
from board.tile import Tile
import pieces
from colorama import Back

# Program constants for each side of the board
from movement import Coordinate
from movement.movement_command import MovementCommand

WHITE = True
BLACK = False


class Board:
    BOARD_SIZE = 8
    tiles = []

    def __init__(self, player_side=WHITE):
        self.__init_board()
        self.player_side = player_side
        self.cpu_side = not player_side
        self.movements = []  # Stack with previous moves
        self.turn = WHITE

    @staticmethod
    def __init_board():
        """Initializes the matrix containing all the board tiles"""
        tiles = []
        for i in range(Board.BOARD_SIZE):
            row = []
            for j in range(Board.BOARD_SIZE):
                row.append(Tile())
            tiles.append(row)

        Board.tiles = tiles
        Board.__place_pieces()
        return tiles

    @staticmethod
    def __place_pieces():
        """Places the contents od the chessboard """
        # Standard black pieces behind the line of pawns
        black_pieces = [pieces.Rook(BLACK), pieces.Knight(BLACK), pieces.Bishop(BLACK), pieces.Queen(BLACK),
                        pieces.King(BLACK), pieces.Bishop(BLACK), pieces.Knight(BLACK), pieces.Rook(BLACK)]

        # Standard white pieces behind the line of pawns
        white_pieces = [pieces.Rook(WHITE), pieces.Knight(WHITE), pieces.Bishop(WHITE), pieces.Queen(WHITE),
                        pieces.King(WHITE), pieces.Bishop(WHITE), pieces.Knight(WHITE), pieces.Rook(WHITE)]

        # Add special pieces
        for i in range(len(Board.tiles[Board.BOARD_SIZE - 1])):
            Board.tiles[Board.BOARD_SIZE - 1][i].piece = white_pieces[i]
            Board.tiles[Board.BOARD_SIZE - 1][i].piece.position = Coordinate(Board.BOARD_SIZE - 1, i)

            Board.tiles[0][i].piece = black_pieces[i]
            Board.tiles[0][i].piece.position = Coordinate(0, i)

        # Lines of pawns
        for j in range(Board.BOARD_SIZE):
            Board.tiles[Board.BOARD_SIZE - 2][j].piece = pieces.Pawn(WHITE)
            Board.tiles[Board.BOARD_SIZE - 2][j].piece.position = Coordinate(Board.BOARD_SIZE - 2, j)

            Board.tiles[1][j].piece = pieces.Pawn(BLACK)
            Board.tiles[1][j].piece.position = Coordinate(1, j)

    @staticmethod
    def get_piece(coordinate):
        return Board.tiles[coordinate.x][coordinate.y].piece

    def move_piece(self, origin, destination):
        piece = Board.get_piece(origin)
        if piece is None or piece.color != self.turn:  # Return no piece or enemy piece was chose
            return False
        # Get all possible moves of the piece and filter those that move to an empty or enemy occupied tile
        legal_moves = piece.get_legal_moves()
        possible_moves = [move for move in legal_moves
                          if Board.get_piece(move) is None or Board.get_piece(move).color != piece.color]
        if destination in possible_moves:  # Execute the movement and store in case the user wants to UNDO it
            movement_command = MovementCommand(piece, origin, destination)
            movement_command.execute()
            self.movements.append(movement_command)
            self.__end_turn()
            return True
        else:
            return False

    def __end_turn(self):
        """Change player turn after checking for checkmate or stalemate"""
        self.__check_stalemate()
        self.__check_checkmate()
        self.turn = not self.turn  # Reverse turns

    def __check_stalemate(self):
        pass

    def __check_checkmate(self):
        pass

    def __str__(self):
        """Returns a human readable representation of the chess board"""
        # Black moves
        self.move_piece(Coordinate(1, 1), Coordinate(3, 1))
        self.move_piece(Coordinate(3, 1), Coordinate(4, 1))
        self.move_piece(Coordinate(4, 1), Coordinate(5, 1))
        self.move_piece(Coordinate(5, 1), Coordinate(6, 2))

        # White move
        self.move_piece(Coordinate(6, 0), Coordinate(4, 0))
        # self.movements.pop().undo()

        column_letters = "  "
        board = ""
        for i in range(self.BOARD_SIZE):
            column_letters += " {} ".format(string.ascii_lowercase[i])
            row_number = str(self.BOARD_SIZE - i)
            board += row_number + "  "
            for j in range(self.BOARD_SIZE):
                if i % 2 != 0 and j % 2 == 0 or i % 2 == 0 and j % 2 != 0:
                    board += Back.LIGHTBLACK_EX
                else:
                    board += Back.LIGHTWHITE_EX

                piece = Board.get_piece(Coordinate(i, j))
                if piece is not None and piece.active is True:
                    board += " {} ".format(piece)
                else:
                    board += "   "

                board += Back.RESET
            board += ("  " + row_number + "\n")
        return column_letters + "\n" + board + column_letters
