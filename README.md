# ja-pychess
Just Another Python Chess is an implementation of a terminal chess game in Python for playing against another player designed as part of the Object Oriented Programming subject.

## Installation
To run the game simply install python and run main.py

## Gameplay
Once the game begins, white side goes first. Yellow tiles are random traps that demote pieces to pawns.
The state of the board is represented in the terminal as follows:
![ja-chess](https://user-images.githubusercontent.com/35763574/67414491-80369780-f5c3-11e9-96b3-c17fd4796587.png)

Type **help** anytime to see the available commands:
-	**help**: show game help
-	**move** **[origin]** **[destination]**: Move the chess piece located in *origin* to the position in *destination* as long as the selected piece belongs to the corresponding player and the defined move is legal. **Example: move a2 a3**
-	**undo**: undo last move
-	**redo**: redo
-	**status**: show whose turn it is, the pieces left on each side and the game board
-	**exec [path/to/file]**: the game interpreter will execute line by line the commands contained in an external file, as long as they are valid
-	**reset**: resets the game
-	**quit**: closes the program
