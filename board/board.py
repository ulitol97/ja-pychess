import random
import re
import string
import sys
from pathlib import Path
from board.tile import Tile
import pieces
from movement import Coordinate
from movement.movement_command import MovementCommand
from colorama import Back, Fore

# Program constants for each side of the board
WHITE = True
BLACK = False
LETTERS = {letter: str(index) for index, letter in enumerate(string.ascii_lowercase, start=1)}


class Board:
    BOARD_SIZE = 8
    tiles = []

    def __init__(self, player_side=WHITE):
        self.__init_board()
        self.player_side = player_side
        self.cpu_side = not player_side
        self.previous_movements = []  # Stack with previous moves
        self.future_movements = []  # Stack with moves to be redone
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
        Board.__place_trap_tiles()
        Board.__place_pieces()
        return tiles

    # All actions triggered by user commands ----------------------------------------------
    @staticmethod
    def action_quit():
        """Exit the game"""
        sys.exit(0)

    def action_help(self):
        """Show game help"""
        print("The available commands are the following:")
        for command in [action.strip() for action in dir(self) if action.startswith("action")]:
            command_name = command.lstrip("action_")
            while len(command_name) < 8:  # Print nicely
                command_name += " "
            print("{0} --> {1}".format(command_name, getattr(self, command).__doc__))
        return False

    def action_reset(self):
        """Restart the state of the board to start a new game from zero"""
        self.turn = WHITE
        print("\nResetting game...\n")
        Board.__init_board()
        return True  # Returning true means the interpreter must re-print the board after executing the command

    def action_move(self, user_input):
        """Move a chess piece of the board if it exists and if it is of your color.
        Format: move <<origin>> <<destiny>>. Example: move a2 a3"""
        # First parse input
        split_input = user_input.split()
        if len(split_input) != 3:
            print("The command has been invoked incorrectly.\nSyntax is: move <<origin>> <<destination>>."
                  "Run like: 'move a2 a3'")
            return False

        # Validate input
        pattern = re.compile("^([a-h][1-8])$")
        if not (pattern.match(split_input[1]) and pattern.match(split_input[2])):
            print("The command has been invoked incorrectly.\nSyntax is: move <<origin>> <<destination>>."
                  "Run like: 'move a2 a3'")
            return False
        else:
            # Command correctly formulated
            origin_coord_y = int(LETTERS[split_input[1][0:1]]) - 1  # Get letter coordinate
            origin_coord_x = Board.BOARD_SIZE - (int(split_input[1][1:]))  # Get number

            dest_coord_y = int(LETTERS[split_input[2][0:1]]) - 1  # Get letter coordinate
            dest_coord_x = Board.BOARD_SIZE - (int(split_input[2][1:]))  # Get number

            moved = self.move_piece(Coordinate(origin_coord_x, origin_coord_y), Coordinate(dest_coord_x, dest_coord_y))
            return moved

    def action_status(self):
        """Show the amount of pieces each color has on the board"""
        game_pieces = []
        for i in range(Board.BOARD_SIZE):
            for j in range(Board.BOARD_SIZE):
                if Board.get_piece(Coordinate(i, j)):
                    game_pieces.append(Board.get_piece(Coordinate(i, j)))

        white_pieces = [piece for piece in game_pieces if piece.color == WHITE]
        black_pieces = [piece for piece in game_pieces if piece.color == BLACK]

        if self.turn == WHITE:
            turn_info = Fore.BLUE + "White" + Fore.RESET + "\n"
        else:
            turn_info = Fore.RED + "Black" + Fore.RESET + "\n"

        print("\n CURRENT TURN: {}".format(turn_info))

        print("\n MATCH STATUS:\n")
        print("\t--> " + Fore.BLUE + "White: " + Fore.RESET + "{0} pieces alive, {1} death.".format(
            len([piece for piece in white_pieces if piece.active is True]),
            len([piece for piece in white_pieces if piece.active is False])))
        print("\t--> " + Fore.RED + "Black: " + Fore.RESET + "{0} pieces alive, {1} death.".format(
            len([piece for piece in black_pieces if piece.active is True]),
            len([piece for piece in black_pieces if piece.active is False])))

        print("\n MATCH BOARD:\n")
        print(self)

        return False

    def action_undo(self):
        """Rewind the match to the moment before you did your previous move"""
        if len(self.previous_movements) == 0:
            print("Can't undo moves if no moves have been made")
            return False
        else:
            # Undo last turn
            prev_move = self.previous_movements.pop()
            self.future_movements.append(prev_move)
            prev_move.undo()
            print("Undone last turns")
            self.turn = not self.turn
            return True

    def action_redo(self):
        """Redo a move that was just undone"""
        if len(self.future_movements) == 0:
            print("Can't redo any moves")
            return False
        else:
            # Redo last undo
            future_move = self.future_movements.pop()
            self.previous_movements.append(future_move)
            future_move.execute()
            print("Undone last turns")
            self.turn = not self.turn
            return True
        pass

    @staticmethod
    def action_exec(input_file):
        """Run all the commands stored in the file specified as input (as long as they are valid).
        Example: exec path-to-file"""
        filepath = Path(input_file.split()[1].strip())
        if not filepath.is_file():
            print("Could not find the input file, did you introduce its path correctly?")
            return False

        with open(filepath) as file:
            commands = file.readlines()

        commands = [x.strip() for x in commands]
        print("FOUND INPUT FILE, EXECUTING CONTENTS:")
        return commands

    # -------------------------------------------------------------------------------------

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
    def __place_trap_tiles():
        trap1_y = random.randint(0, Board.BOARD_SIZE-1)
        trap2_y = random.randint(0, Board.BOARD_SIZE-1)

        Board.tiles[Board.BOARD_SIZE//2 - 1][trap1_y].trap = True
        Board.tiles[Board.BOARD_SIZE//2][trap2_y].trap = True


    @staticmethod
    def get_piece(coordinate):
        return Board.tiles[coordinate.x][coordinate.y].piece

    def move_piece(self, origin, destination):
        piece = Board.get_piece(origin)
        if piece is None:  # Return no piece or enemy piece was chose
            print("Can not move piece that does not exist in the selected location")
            return False
        if piece.color != self.turn:
            print("Can not move a piece that does not belong to you!")
            return False

        # Get all possible moves of the piece and filter those that move to an empty or enemy occupied tile
        legal_moves = piece.get_legal_moves()
        possible_moves = [move for move in legal_moves
                          if Board.get_piece(move) is None or Board.get_piece(move).color != piece.color]

        if destination in possible_moves:  # Execute the movement and store in case the user wants to UNDO it
            movement_command = MovementCommand(piece, origin, destination)
            movement_command.execute()
            self.previous_movements.append(movement_command)
            self.future_movements = []
            self.__end_turn()
            return True
        else:
            print("A piece was selected, but the input destination was not right")
            return False

    def __end_turn(self):
        """Change player turn after checking for checkmate or stalemate"""
        self.__check_check()
        self.turn = not self.turn  # Reverse turns

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
            Board.action_reset(self)

    def __str__(self):
        """Returns a human readable representation of the chess board"""
        column_letters = "   "
        board = ""
        for i in range(self.BOARD_SIZE):
            column_letters += " {} ".format(string.ascii_lowercase[i])
            row_number = str(self.BOARD_SIZE - i)
            board += row_number + "  "
            for j in range(self.BOARD_SIZE):
                if Board.tiles[i][j].trap is True:
                    board += Back.LIGHTYELLOW_EX
                else:
                    if i % 2 != 0 and j % 2 == 0 or i % 2 == 0 and j % 2 != 0:
                        board += Back.LIGHTBLACK_EX
                    else:
                        board += Back.LIGHTWHITE_EX

                board += " {} ".format(self.tiles[i][j])
                board += Back.RESET
            board += ("  " + row_number + "\n")
        return column_letters + "\n" + board + column_letters
