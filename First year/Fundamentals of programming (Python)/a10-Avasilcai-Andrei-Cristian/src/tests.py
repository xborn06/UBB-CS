import unittest
from unittest.mock import MagicMock
from src.computer_strategy import ComputerStrategy
from src.board import MillBoard
from src.game import MillGame

class TestComputerStrategy(unittest.TestCase):
    def setUp(self):
        self.board = MillBoard()
        self.game = MillGame(self.board, 1)
        self.strategy = ComputerStrategy(self.game)

    def test_best_move_placement_phase(self):
        self.game.board.__free_positions = [(0, 0), (0, 3), (0, 6), (6, 0), (6, 6), (3, 0), (3, 6), (6, 3)]
        move = self.strategy.best_move(1)
        self.assertIn(move, [(0, 0), (0, 3), (0, 6), (6, 0), (6, 6), (3, 0), (3, 6), (6, 3)])

    def test_best_move_moving_phase(self):
        self.game.computer_positions = [(0, 0)]
        self.game.board.__free_positions = [(0, 3)]
        self.game.board.is_adjacent = MagicMock(return_value=True)
        self.strategy.evaluate_position_impact = MagicMock(return_value=10)
        move = self.strategy.best_move(2)
        self.assertEqual(move, ((0, 0), (0, 0)))

    def test_best_move_flying_phase(self):
        self.game.computer_positions = [(0, 0)]
        self.game.board.__free_positions = [(0, 3)]
        self.strategy.evaluate_position_impact = MagicMock(return_value=10)
        move = self.strategy.best_move(3)
        self.assertEqual(move, ((0, 0), (0, 0)))

    def test_blocks_first_mill_attempt(self):
        self.game.board.get_position_value = MagicMock(return_value=0)
        self.game.board.set_position_value = MagicMock()
        self.game.board.get_possible_mills = MagicMock(return_value=[[(0, 0), (0, 3), (0, 6)]])
        self.game.board.get_position_value.side_effect = [0, 1, 1]
        result = self.strategy.blocks_first_mill_attempt(0, 0)
        self.assertTrue(result)

    def test_would_create_mill(self):
        self.game.board.get_position_value = MagicMock(return_value=0)
        self.game.board.set_position_value = MagicMock()
        self.game.board.get_possible_mills = MagicMock(return_value=[[(0, 0), (0, 3), (0, 6)]])
        self.game.board.get_position_value.side_effect = [0, 2, 2, 2]
        result = self.strategy.would_create_mill(0, 0, "computer")
        self.assertTrue(result)

    def test_evaluate_position(self):
        self.strategy.creates_mill = MagicMock(side_effect=[True, False, True, False])
        computer_positions = [(0, 0), (0, 3)]
        player_positions = [(0, 6), (1, 1)]
        score = self.strategy.evaluate_position(computer_positions, player_positions)
        self.assertEqual(score, 0)

    def test_evaluate_best_position_to_remove(self):
        self.game.board.check_three_in_a_row = MagicMock(return_value=False)
        self.strategy.evaluate_position_impact = MagicMock(side_effect=[10, 5, 15])
        player_positions = [(0, 0), (0, 3), (0, 6)]
        computer_positions = [(1, 1), (1, 3)]
        best_position = self.strategy.evaluate_best_position_to_remove(player_positions, computer_positions)
        self.assertEqual(best_position, (0, 3))

    def test_evaluate_position_impact(self):
        self.game.board.get_position_value = MagicMock(return_value=0)
        self.game.board.set_position_value = MagicMock()
        self.game.board.get_possible_mills = MagicMock(return_value=[[(0, 0), (0, 3), (0, 6)]])
        self.game.board.is_adjacent = MagicMock(return_value=True)
        player_positions = [(0, 3)]
        computer_positions = [(1, 1)]
        impact = self.strategy.evaluate_position_impact((0, 0), player_positions, computer_positions)
        self.assertEqual(impact, 3)

class TestMillGame(unittest.TestCase):
    def setUp(self):
        self.board = MillBoard()
        self.game = MillGame(self.board, 1)

    def test_initialization(self):
        self.assertEqual(self.game.stage, 1)
        self.assertEqual(self.game.remaining_player_pieces, 9)
        self.assertEqual(self.game.remaining_computer_pieces, 9)
        self.assertEqual(self.game.player_pieces, 0)
        self.assertEqual(self.game.computer_pieces, 0)
        self.assertEqual(self.game.player_positions, [])
        self.assertEqual(self.game.computer_positions, [])

    def test_check_stalemate(self):
        self.game.count_adjacent_free_positions = MagicMock(return_value=0)
        self.assertTrue(self.game.check_stalemate())

    def test_win_check(self):
        self.game.stage = 2
        self.game.player_pieces = 2
        self.game.computer_pieces = 3
        self.assertEqual(self.game.win_check(), 1)
        self.game.player_pieces = 3
        self.game.computer_pieces = 2
        self.assertEqual(self.game.win_check(), 2)
        self.game.player_pieces = 3
        self.game.computer_pieces = 3
        self.game.count_adjacent_free_positions = MagicMock(side_effect=[0, 1])
        self.assertEqual(self.game.win_check(), 1)
        self.game.count_adjacent_free_positions = MagicMock(side_effect=[1, 0])
        self.assertEqual(self.game.win_check(), 2)

    def test_remove_pieces(self):
        self.game.computer_positions = [(0, 0)]
        self.game.remove_pieces("computer", (0, 0))
        self.assertEqual(self.game.computer_positions, [])
        self.assertEqual(self.game.computer_pieces, -1)
        self.game.player_positions = [(1, 1)]
        self.game.remove_pieces("player", (1, 1))
        self.assertEqual(self.game.player_positions, [])
        self.assertEqual(self.game.player_pieces, -1)

    def test_computer_move(self):
        self.board.place = MagicMock()
        self.board.move = MagicMock()
        self.board.free_move = MagicMock()
        move = (0, 0)
        self.game.computer_stage = 1
        self.assertEqual(self.game.computer_move(move), move)
        self.game.computer_positions = [(0, 0)]
        move = ((0, 0), (0, 1))
        self.game.computer_stage = 2
        self.assertEqual(self.game.computer_move(move), (0, 1))
        self.game.computer_positions = [(0, 0)]
        move = ((0, 0), (0, 1))
        self.game.computer_stage = 3
        self.assertEqual(self.game.computer_move(move), (0, 1))

    def test_player_move(self):
        self.board.place = MagicMock()
        self.board.move = MagicMock()
        self.board.free_move = MagicMock()
        move = (0, 0)
        self.game.player_stage = 1
        self.assertIsNone(self.game.player_move(move))
        self.game.player_positions = [(0, 0)]
        move = ((0, 0), (0, 1))
        self.game.player_stage = 2
        self.assertIsNone(self.game.player_move(move))
        self.game.player_positions = [(0, 0)]
        move = ((0, 0), (0, 1))
        self.game.player_stage = 3
        self.assertIsNone(self.game.player_move(move))

if __name__ == '__main__':
    unittest.main()