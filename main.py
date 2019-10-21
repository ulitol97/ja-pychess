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
    player_choice = input(">> On which side would you like to play: black or white [wB]? ").lower()
    if 'w' in player_choice:
        print("You will play as " + Fore.BLUE + "white" + Fore.RESET)
        return board.WHITE
    else:
        print("You will play as " + Fore.RED + "black" + Fore.RESET)
        return board.BLACK


def run_game(game_board):
    """Start the infinite interpreter loop"""
    print("Turn of " + Fore.BLUE + "white" + Fore.RESET)
    print(game_board)
    while True:
        # while True:
        print()
        invalid_command = True
        print_board = True

        while invalid_command is True:
            player_command = input(">> Run a command or type 'help' for information:\n").lower()
            command_keywords = player_command.split()
            print(command_keywords)
            if command_prefix+command_keywords[0] in [action.strip() for action in dir(game_board) if action.startswith("action")]:
                # Existing command, try to run it
                # try:

                    if len(command_keywords) == 1:
                        print_board = getattr(game_board, command_prefix+player_command)()
                    else:
                        print_board = getattr(game_board, command_prefix + command_keywords[0])(player_command)
                    invalid_command = False
                # except:
                #     print ("There was a problem executing your instruction")
                #     invalid_command = True
                #     invalid_command = False
                # finally:
                #     print()
            else:
                # Invalid command, try again
                print("Please introduce a valid command. Check more information by typing 'help'.")

        if print_board is True:
            if game_board.turn == board.WHITE:
                print("Turn of " + Fore.BLUE + "white" + Fore.RESET)
            else:
                print("Turn of " + Fore.RED + "black" + Fore.RESET)
            print (game_board)
        # Input command


init()
player_side = ask_player_side()
command_prefix = "action_"
game_board = board.Board(player_side)
run_game(game_board)
