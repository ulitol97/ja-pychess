import string
from board.tile import Tile
import pieces
from colorama import Back, Fore

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
        # Keep track of each side king
        self.white_king = Board.get_piece(Coordinate(7, 4))
        self.black_king = Board.get_piece(Coordinate(0, 4))

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
    def action_reset():
        print("\nResetting game...\n")
        Board.__init_board()

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
        self.__check_check()
        # self.turn = not self.turn  # Reverse turns

    def __check_check(self):
        """Check if, after doing a move, the rival is in check ("jaque")"""
        player_next_moves = []
        for i in range(Board.BOARD_SIZE):
            for j in range(Board.BOARD_SIZE):
                piece = Board.get_piece(Coordinate(i, j))
                if piece is not None and piece.color == self.turn:
                    player_next_moves += [move for move in piece.get_legal_moves()
                                          if
                                          Board.get_piece(move) is None or Board.get_piece(move).color != piece.color]
        #  We have collected all the places the player can move his pieces.
        #  If the rival king is among them, its check.
        if self.turn == WHITE:
            if self.black_king.position in player_next_moves:
                print("The " + Fore.RED + "black king" + Fore.RESET + " is in check!")
                self.__check_checkmate(player_next_moves)
        else:
            if self.white_king.position in player_next_moves:
                print("The " + Fore.BLUE + "white king" + Fore.BLUE + " is in check!")
                self.__check_checkmate(player_next_moves)

    def __check_checkmate(self, player_movements):
        """Check if, after doing a move, the rival is in checkmate ("jaque mate")"""
        checkmate = True
        if self.turn == WHITE:
            king_movements = self.black_king.get_legal_moves()
            king_movements = [move for move in king_movements
                              if Board.get_piece(move) is None or Board.get_piece(move).color != BLACK]
        else:
            king_movements = self.white_king.get_legal_moves()
            king_movements = [move for move in king_movements
                              if Board.get_piece(move) is None or Board.get_piece(move).color != WHITE]

        for move in king_movements:
            if move not in player_movements:  # King escaped checkmate
                checkmate = False

        if checkmate is True:
            if self.turn == WHITE:
                print("The " + Fore.RED + "black king" + Fore.RESET + " is in checkmate!")
                print(Fore.BLUE + "White side wins!" + Fore.RESET)
            else:
                print("The " + Fore.BLUE + "white king" + Fore.RESET + " is in checkmate!")
                print(Fore.RED + "Black side wins!" + Fore.RESET)

            #  Reset game
            Board.action_reset()

    def __str__(self):
        """Returns a human readable representation of the chess board"""
        # Black moves
        self.move_piece(Coordinate(1, 1), Coordinate(3, 1))
        self.move_piece(Coordinate(3, 1), Coordinate(4, 1))
        self.move_piece(Coordinate(4, 1), Coordinate(5, 1))
        self.move_piece(Coordinate(5, 1), Coordinate(6, 2))

        # White move
        # self.move_piece(Coordinate(6, 2), Coordinate(4, 2))
        # self.move_piece(Coordinate(4, 2), Coordinate(3, 2))
        # self.move_piece(Coordinate(3, 2), Coordinate(2, 2))
        # self.move_piece(Coordinate(2, 2), Coordinate(1, 3))

        self.move_piece(Coordinate(6, 3), Coordinate(5, 3))

        # #Pawn 2
        # self.move_piece(Coordinate(6, 0), Coordinate(4, 0))
        # self.move_piece(Coordinate(4, 0), Coordinate(3, 0))
        # self.move_piece(Coordinate(3, 0), Coordinate(2, 0))
        # self.move_piece(Coordinate(2, 0), Coordinate(1, 1))

        # Rook
        for move in Board.get_piece(Coordinate(7,0)).get_legal_moves():
            print(move)
        self.move_piece(Coordinate(7, 0), Coordinate(1, 0))

        # Knight
        self.move_piece(Coordinate(7, 1), Coordinate(6, 3))
        self.move_piece(Coordinate(6, 3), Coordinate(4, 4))
        self.move_piece(Coordinate(4, 4), Coordinate(2, 5))



        # Queen
        self.move_piece(Coordinate(7, 3), Coordinate(6, 2))
        self.move_piece(Coordinate(6, 2), Coordinate(2, 2))
        # self.move_piece(Coordinate(2, 2), Coordinate(2, 4))
        # self.movements.pop().undo()

        column_letters = "   "
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
