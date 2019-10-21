import unittest
from typing import List

from board import board
from movement import Coordinate
from pieces import Piece, Pawn


class TestUM(unittest.TestCase):
    """
    Unit tests of the Board class
    For these tests we create a game board and internally change its chess pieces and properties to check
    the functionality is working fine
    """

    def setUp(self):
        print("Executing test of board...")

    def test_board_constructor(self):
        """Initialize a new game board and check the all inner data has been stored correctly"""
        game_board = board.Board(board.WHITE)  # Start a new board
        self.assertEqual(board.WHITE, True)
        self.assertEqual(board.BLACK, False)
        self.assertEqual(game_board.turn, board.WHITE)
        self.assertEqual(game_board.player_side, board.WHITE)
        self.assertEqual(game_board.rival_side, board.BLACK)
        self.assertIs(len(game_board.previous_movements), 0)
        self.assertIs(len(game_board.future_movements), 0)

        self.assertEqual(game_board.white_king.__class__.__name__, "King")
        self.assertEqual(game_board.white_king.position, Coordinate(7, 4))
        self.assertEqual(game_board.black_king.__class__.__name__, "King")
        self.assertEqual(game_board.black_king.position, Coordinate(0, 4))

    def test_board_trap(self):
        """Create artificial traps and make pieces fall onto them to check their functionality"""
        # Start a new board
        game_board = board.Board(board.WHITE)
        # Create trap tiles
        board.Board.tiles[5][0].trap = True
        # Make a Pawn fall into trap, nothing changes

        piece: Piece = board.Board.get_piece(Coordinate(6, 0))
        self.assertTrue(piece.__class__.__name__ is "Pawn")
        game_board.move_piece(piece.position, Coordinate(5, 0))
        self.assertTrue(piece.__class__.__name__ is "Pawn")

        # Start a new board
        game_board = board.Board(board.WHITE)
        # Create trap tiles
        board.Board.tiles[5][0].trap = True
        piece: Piece = board.Board.get_piece(Coordinate(6, 0))
        game_board.move_piece(piece.position, Coordinate(4, 0))

        # Manually change to our turn and make a Rook fall in the trap
        game_board.turn = piece.color
        piece = board.Board.get_piece(Coordinate(7, 0))
        self.assertTrue(piece.__class__.__name__ is "Rook")
        game_board.move_piece(piece.position, Coordinate(5, 0))
        self.assertTrue(piece.__class__.__name__ is "Pawn")

    def test_check(self):
        """
        Create a game situation in which one of the kings is in check ('jaque') adn then checkmate ('jaque mate')
        to test the detection algorithm
        """
        # Start a new board
        game_board = board.Board(board.WHITE)

        # Move pawn to let Rook exit
        piece: Piece = board.Board.get_piece(Coordinate(6, 0))
        self.assertTrue(piece.__class__.__name__ is "Pawn")
        game_board.move_piece(piece.position, Coordinate(4, 0))

        # Select rook
        piece: Piece = board.Board.get_piece(Coordinate(7, 0))
        self.assertTrue(piece.__class__.__name__ is "Rook")

        # Manually change to our turn and make the Rook corner the enemy king
        game_board.turn = piece.color
        game_board.move_piece(piece.position, Coordinate(5, 0))
        self.assertEqual(piece.position.x, 5)
        self.assertEqual(piece.position.y, 0)
        game_board.turn = piece.color
        game_board.move_piece(piece.position, Coordinate(5, 4))
        self.assertEqual(piece.position.x, 5)
        self.assertEqual(piece.position.y, 4)
        game_board.turn = piece.color
        game_board.move_piece(piece.position, Coordinate(1, 4))
        self.assertEqual(piece.position.x, 1)
        self.assertEqual(piece.position.y, 4)

        # The black king should be in check
        game_board.turn = piece.color
        self.assertTrue(game_board.check_check())

        # Move rook backwards to create checkmate
        game_board.move_piece(piece.position, Coordinate(2, 4))
        game_board.turn = piece.color
        self.assertTrue(game_board.check_checkmate(piece.get_legal_moves()))

    def test_undo_redo(self):
        """
        Create a game situation in which undoing the previous action may cause one piece to be alive again, etc.
        and try redoing it as well
        """
        # Start a new board
        game_board = board.Board(board.WHITE)
        self.assertFalse(game_board.action_undo())
        self.assertFalse(game_board.action_redo())

        # Move pawn to let Rook exit and check undo and redo work for just changes in position
        piece: Piece = board.Board.get_piece(Coordinate(6, 0))
        self.assertTrue(piece.__class__.__name__ is "Pawn")
        game_board.move_piece(piece.position, Coordinate(4, 0))
        self.assertEqual(piece.position.x, 4)
        self.assertEqual(piece.position.y, 0)
        game_board.action_undo()
        self.assertEqual(piece.position.x, 6)
        self.assertEqual(piece.position.y, 0)
        game_board.action_redo()
        self.assertEqual(piece.position.x, 4)
        self.assertEqual(piece.position.y, 0)

        # Select rook
        piece: Piece = board.Board.get_piece(Coordinate(7, 0))
        self.assertTrue(piece.__class__.__name__ is "Rook")

        # Manually change to our turn and make the Rook corner the enemy king
        game_board.turn = piece.color
        game_board.move_piece(piece.position, Coordinate(5, 0))
        self.assertEqual(piece.position.x, 5)
        self.assertEqual(piece.position.y, 0)
        game_board.turn = piece.color
        game_board.move_piece(piece.position, Coordinate(5, 4))
        self.assertEqual(piece.position.x, 5)
        self.assertEqual(piece.position.y, 4)

        # Kill the black pawn
        game_board.turn = piece.color
        self.assertEqual(board.Board.tiles[1][4].piece.__class__.__name__, "Pawn")
        self.assertEqual(board.Board.get_piece(Coordinate(1, 4)).color, board.BLACK)

        game_board.move_piece(piece.position, Coordinate(1, 4))
        self.assertEqual(piece.position.x, 1)
        self.assertEqual(piece.position.y, 4)

        self.assertEqual(board.Board.tiles[1][4].piece.__class__.__name__, "Rook")
        self.assertEqual(board.Board.get_piece(Coordinate(1, 4)).color, board.WHITE)

        # Undo the movement that killed the pawn
        game_board.action_undo()
        self.assertEqual(board.Board.tiles[1][4].piece.__class__.__name__, "Pawn")
        self.assertEqual(board.Board.get_piece(Coordinate(1, 4)).color, board.BLACK)
        self.assertEqual(board.Board.tiles[5][4].piece.__class__.__name__, "Rook")
        self.assertEqual(board.Board.get_piece(Coordinate(5, 4)).color, board.WHITE)

        # Redo the movement that killed the pawn
        game_board.action_redo()
        # The black king should be in check after that move
        game_board.turn = piece.color
        self.assertTrue(game_board.check_check())


if __name__ == "__main__":
    unittest.main()
