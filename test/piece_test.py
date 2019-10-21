import unittest
from typing import List

from board import board
from movement import Coordinate
from pieces import Piece, Pawn


class TestUM(unittest.TestCase):
    """
    Unit tests of the Piece class
    For these tests we create different pieces and make them move along the board and interact with each other
    to check that the movement logic is correct
    """

    def setUp(self):
        print("Executing test of pieces...")

    def test_piece_constructor_abstract(self):
        """Check an abstract piece cannot be created."""
        self.assertRaises(TypeError, Piece())

    def test_piece_constructor(self):
        """Initialize any piece and check the all inner data has been stored correctly"""
        pawn: Pawn = Pawn(board.WHITE)
        self.assertEqual(pawn.color, board.WHITE)
        self.assertTrue(pawn.position.x is None)
        self.assertTrue(pawn.position.y is None)
        self.assertTrue(pawn.active)
        self.assertFalse(pawn.has_moved)

    def test_pawn_movement(self):
        """Initialize a board, choose a pawn piece and check the chess rules work correctly"""
        game_board = board.Board(board.WHITE)  # Start a new board

        piece: Piece = board.Board.get_piece(Coordinate(6, 0))
        self.assertTrue(piece.__class__.__name__ is "Pawn")
        self.assertTrue(piece.position.x == 6)
        self.assertTrue(piece.position.y == 0)
        self.assertEqual(piece.color, board.WHITE)

        # First move, pawn can advance two tiles or one
        legal_moves: List[Coordinate] = piece.get_legal_moves()
        self.assertIs(len(legal_moves), 2)

        game_board.move_piece(piece.position, Coordinate(4, 0))
        self.assertTrue(piece.position.x == 4)
        self.assertTrue(piece.position.y == 0)
        self.assertTrue(piece.has_moved)

        # Nor first move, pawn can advance one tile
        legal_moves = piece.get_legal_moves()
        self.assertIs(len(legal_moves), 1)

        # This movement is ignored because after each move the board changes the player in control
        game_board.move_piece(piece.position, Coordinate(3, 0))
        self.assertTrue(piece.position.x == 4)
        self.assertTrue(piece.position.y == 0)

        # Manually change to our turn
        game_board.turn = piece.color
        game_board.move_piece(piece.position, Coordinate(3, 0))
        self.assertTrue(piece.position.x == 3)
        self.assertTrue(piece.position.y == 0)
        game_board.turn = piece.color
        game_board.move_piece(piece.position, Coordinate(2, 0))
        self.assertTrue(piece.position.x == 2)
        self.assertTrue(piece.position.y == 0)

        # Where are facing a line of pawns not, we can eat one of them
        legal_moves = piece.get_legal_moves()
        self.assertIs(len(legal_moves), 1)

        self.assertIs(board.Board.get_piece(Coordinate(1, 1)).color, board.BLACK)

        # Eat the pawn in 1, 1
        game_board.turn = piece.color
        game_board.move_piece(piece.position, Coordinate(1, 1))
        self.assertTrue(piece.position.x == 1)
        self.assertTrue(piece.position.y == 1)
        self.assertIs(board.Board.get_piece(Coordinate(1, 1)).color, board.WHITE)

    def test_knight_movement(self):
        """Initialize a board, choose a knight piece and check the chess rules work correctly"""
        game_board = board.Board(board.WHITE)  # Start a new board

        piece: Piece = board.Board.get_piece(Coordinate(7, 1))
        self.assertTrue(piece.__class__.__name__ is "Knight")
        self.assertTrue(piece.position.x == 7)
        self.assertTrue(piece.position.y == 1)
        self.assertEqual(piece.color, board.WHITE)

        # First move, knight can advance in two ways
        legal_moves: List[Coordinate] = [move for move in piece.get_legal_moves()
                                         if board.Board.get_piece(move) is None or board.Board.get_piece(move).color
                                         != piece.color or board.Board.get_piece(move).active is False]

        self.assertIs(len(legal_moves), 2)

        game_board.move_piece(piece.position, Coordinate(5, 0))
        self.assertTrue(piece.position.x == 5)
        self.assertTrue(piece.position.y == 0)
        self.assertTrue(piece.has_moved)

        # Manually change to our turn and check available moves
        game_board.turn = piece.color
        legal_moves = [move for move in piece.get_legal_moves()
                                         if board.Board.get_piece(move) is None or board.Board.get_piece(move).color
                                         != piece.color or board.Board.get_piece(move).active is False]

        self.assertIs(len(legal_moves), 3)
        game_board.move_piece(piece.position, Coordinate(5, 0))
        self.assertTrue(piece.position.x == 5)
        self.assertTrue(piece.position.y == 0)

    def test_rook_movement(self):
        """Initialize a board, choose a rook piece and check the chess rules work correctly"""
        game_board = board.Board(board.WHITE)  # Start a new board

        piece: Piece = board.Board.get_piece(Coordinate(7, 0))
        self.assertTrue(piece.__class__.__name__ is "Rook")
        self.assertTrue(piece.position.x == 7)
        self.assertTrue(piece.position.y == 0)
        self.assertEqual(piece.color, board.WHITE)

        # Artificially remove the front pawn out of the way to allow rook movement
        board.Board.get_piece(Coordinate(6, 0)).active = False

        # First move, rook can advance forward
        legal_moves: List[Coordinate] = [move for move in piece.get_legal_moves()
                                         if board.Board.get_piece(move) is None or board.Board.get_piece(move).color
                                         != piece.color or board.Board.get_piece(move).active is False]

        self.assertIs(len(legal_moves), 6)
        game_board.turn = piece.color
        game_board.move_piece(piece.position, Coordinate(2, 0))
        self.assertTrue(piece.position.x == 2)
        self.assertTrue(piece.position.y == 0)

        game_board.turn = piece.color
        game_board.move_piece(piece.position, Coordinate(2, 7))
        self.assertTrue(piece.position.x == 2)
        self.assertTrue(piece.position.y == 7)

    def test_bishop_movement(self):
        """Initialize a board, choose a bishop piece and check the chess rules work correctly"""
        game_board = board.Board(board.WHITE)  # Start a new board

        piece: Piece = board.Board.get_piece(Coordinate(7, 2))
        self.assertTrue(piece.__class__.__name__ is "Bishop")
        self.assertTrue(piece.position.x == 7)
        self.assertTrue(piece.position.y == 2)
        self.assertEqual(piece.color, board.WHITE)

        # Artificially remove the front side pawns out of the way to allow bishop movement
        board.Board.get_piece(Coordinate(6, 1)).active = False
        board.Board.get_piece(Coordinate(6, 3)).active = False

        # First move, bishop diagonal
        legal_moves: List[Coordinate] = [move for move in piece.get_legal_moves()
                                         if board.Board.get_piece(move) is None or board.Board.get_piece(move).color
                                         != piece.color or board.Board.get_piece(move).active is False]

        self.assertIs(len(legal_moves), 7)
        game_board.turn = piece.color
        game_board.move_piece(piece.position, Coordinate(5, 0))
        self.assertTrue(piece.position.x == 5)
        self.assertTrue(piece.position.y == 0)

        # Second move, return home
        game_board.turn = piece.color
        game_board.move_piece(piece.position, Coordinate(7, 2))
        self.assertTrue(piece.position.x == 7)
        self.assertTrue(piece.position.y == 2)

        # Third move, try the other diagonal
        game_board.turn = piece.color
        game_board.move_piece(piece.position, Coordinate(2, 7))
        self.assertTrue(piece.position.x == 2)
        self.assertTrue(piece.position.y == 7)

    # The queen functionality relies solely on the rook and bishop functionality, so we need not test it if
    # we already test the other two

    def test_king_movement(self):
        """Initialize a board, choose a king piece and check the chess rules work correctly"""
        game_board = board.Board(board.WHITE)  # Start a new board

        piece: Piece = board.Board.get_piece(Coordinate(7, 4))
        self.assertTrue(piece.__class__.__name__ is "King")
        self.assertTrue(piece.position.x == 7)
        self.assertTrue(piece.position.y == 4)
        self.assertEqual(piece.color, board.WHITE)

        # Fake move, king can not move because it is surrounded by other allies
        legal_moves: List[Coordinate] = [move for move in piece.get_legal_moves()
                                         if board.Board.get_piece(move) is None or board.Board.get_piece(move).color
                                         != piece.color or board.Board.get_piece(move).active is False]

        self.assertIs(len(legal_moves), 0)
        game_board.turn = piece.color
        game_board.move_piece(piece.position, Coordinate(6, 3))
        self.assertTrue(piece.position.x == 7)  # Unchanged
        self.assertTrue(piece.position.y == 4)

        # Artificially remove the front and side pawns out of the way to allow king movement
        board.Board.get_piece(Coordinate(6, 3)).active = False
        board.Board.get_piece(Coordinate(6, 4)).active = False
        board.Board.get_piece(Coordinate(6, 5)).active = False

        # First move, king can move diagonally
        legal_moves = [move for move in piece.get_legal_moves()
                                         if board.Board.get_piece(move) is None or board.Board.get_piece(move).color
                                         != piece.color or board.Board.get_piece(move).active is False]

        self.assertIs(len(legal_moves), 3)
        game_board.turn = piece.color
        game_board.move_piece(piece.position, Coordinate(6, 3))
        self.assertTrue(piece.position.x == 6)
        self.assertTrue(piece.position.y == 3)

        # Second move, return home
        game_board.turn = piece.color
        game_board.move_piece(piece.position, Coordinate(7, 4))
        self.assertTrue(piece.position.x == 7)
        self.assertTrue(piece.position.y == 4)

        # Third move, try moving forward
        game_board.turn = piece.color
        game_board.move_piece(piece.position, Coordinate(6, 4))
        self.assertTrue(piece.position.x == 6)
        self.assertTrue(piece.position.y == 4)


if __name__ == "__main__":
    unittest.main()
