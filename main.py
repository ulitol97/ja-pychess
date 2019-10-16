"""
The current module defines the application entry-point, consisting of:
    -> A command interpreter:
         - Running in an endless loop awaiting user commands
         - Capable of parsing user commands (unrecognized commands will not be taken into account)
         - Capable of loading commands from a file
"""
from board import Board

# Program constants for each side of the board
WHITE = True
BLACK = False


class Interpreter:
    def __init__(self):
        self.board = Board()
    