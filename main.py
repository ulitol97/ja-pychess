"""
The current module defines the application entry-point, consisting of:
    -> A command interpreter:
         - Running in an endless loop awaiting user commands
         - Capable of parsing user commands (unrecognized commands will not be taken into account)
         - Capable of loading commands from a file
"""
from board import board
from colorama import init, Fore


def ask_player_side():
    """Greet the player and prompt the player to enter the side of the chessboard he/she would like to play as"""

    print("Welcome to 'Just Another Python Chess'")
    player_choice = input("On which side would you like to play: black or white [wB]? ").lower()
    if 'w' in player_choice:
        print("You will play as " + Fore.BLUE + "white" + Fore.RESET)
        return board.WHITE
    else:
        print("You will play as " + Fore.RED + "black" + Fore.RESET)
        return board.BLACK


def run_game(game_board):
    """Start the infinite interpreter loop"""
    # while True:
    print()
    if game_board.turn == board.WHITE:
        print("Turn of " + Fore.BLUE + "white" + Fore.RESET)
    else:
        print("Turn of " + Fore.RED + "black" + Fore.RESET)
    print (game_board)
    # Input command
    print()


init()
player_side = ask_player_side()
game_board = board.Board(player_side)
run_game(game_board)
