"""
The main module defines the application entry-point, consisting of:
    -> A command interpreter:
         - Running in an endless loop awaiting user commands
         - Capable of parsing user commands (unrecognized commands will not be taken into account)
         - Capable of loading commands from a file
"""
from typing import List, Union, Tuple

from board import board
from colorama import init, Fore


def ask_player_side() -> bool:
    """Greet the player and prompt the player to enter the side of the chessboard he/she would like to play as.
    This id formality as for now the player will control both sides"""

    print("Welcome to 'Just Another Python Chess'")
    player_choice: str = input(">> On which side would you like to play: black or white [wB]? ").lower()
    if 'w' in player_choice:
        print("You will play as " + Fore.BLUE + "white" + Fore.RESET)
        return board.WHITE
    else:
        print("You will play as " + Fore.RED + "black" + Fore.RESET)
        return board.BLACK


def parse_and_run_command(player_command: str) -> Tuple[bool, Union[bool, List[str]]]:
    """Execute a command given the user input in the interpreter.
    Evaluate the command and tell the interpreter whether if it was valid or not"""
    invalid_command: bool = True
    print_board: Union[bool, List[str]] = False

    command_keywords: List[str] = player_command.split()
    if command_prefix + command_keywords[0] in [action.strip() for action in dir(game_board) if
                                                action.startswith("action")]:
        # Existing command, try to run it
        try:
            if len(command_keywords) == 1:  # Command with no arguments
                print_board = getattr(game_board, command_prefix + player_command)()
            else:  # Command with arguments
                print_board = getattr(game_board, command_prefix + command_keywords[0])(player_command)
            invalid_command = False
        except SystemExit:  # Allow system to exit, catch all other exceptions
            raise
        except:  # For other exceptions, show a warning message and hide stack trace to user
            print("There was a problem executing your instruction. Type 'help' to see available commands.")
            invalid_command = True
        finally:
            print()
    else:
        # Invalid command, try again
        print("Please introduce a valid command. Check more information by typing 'help'.")

    # Return a tuple with the values the interpreter needs to know what to do
    return invalid_command, print_board


def run_game(game_board) -> None:
    """Start the infinite interpreter loop. Ask for commands and print the state of the board after their execution"""
    print("Turn of " + Fore.BLUE + "white" + Fore.RESET)
    print(game_board)
    while True:
        # while True:
        print()
        invalid_command: bool = True
        print_board: Union[bool, List[str]] = True

        while invalid_command is True:
            player_command: str = input(">> Run a command or type 'help' for information: ").lower()
            results = parse_and_run_command (player_command)
            invalid_command = results[0]
            print_board = results[1]
            if isinstance(print_board, list):
                # Special case when we are executing code from a file. Run each command.
                for command in print_board:
                    print ("\t --> {}...".format(command))
                    parse_and_run_command(command)
                print ("FINISHED EXECUTING FILE COMMANDS:\n")
                print (game_board)

        if print_board is True:
            if game_board.turn == board.WHITE:
                print("Turn of " + Fore.BLUE + "white" + Fore.RESET)
            else:
                print("Turn of " + Fore.RED + "black" + Fore.RESET)
            print(game_board)


# Beginning of the main script ----------------------------------------------
init()  # Allow printing in color
player_side: bool = ask_player_side()  # Get player side
command_prefix: str = "action_"  # Define the nomenclature of the methods of the board the user can access
game_board: board.Board = board.Board(player_side)  # Start a new board
run_game(game_board)  # Start the interpreter
