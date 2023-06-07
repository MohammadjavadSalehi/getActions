import unittest
from unittest.mock import patch
from io import StringIO
import random

from rps_game import play_game, run_game


class TestRPSGame(unittest.TestCase):
    def test_play_game_tie(self):
        # Test that the function correctly handles a tie
        with patch('builtins.input', return_value='rock'), patch('sys.stdout', new=StringIO()) as fake_output:
            random.seed(1)
            play_game()
            self.assertEqual(fake_output.getvalue().strip(), "It's a tie!")

    def test_play_game_win(self):
        # Test that the function correctly handles a win
        with patch('builtins.input', return_value='paper'), patch('sys.stdout', new=StringIO()) as fake_output:
            random.seed(2)
            play_game()
            self.assertEqual(fake_output.getvalue().strip(), "You win!")

    def test_play_game_loss(self):
        # Test that the function correctly handles a loss
        with patch('builtins.input', return_value='scissors'), patch('sys.stdout', new=StringIO()) as fake_output:
            random.seed(3)
            play_game()
            self.assertEqual(fake_output.getvalue().strip(), "You lose!")

    def test_run_game(self):
        # Test that the function runs without errors
        with patch('builtins.input', side_effect=['rock', 'no']), patch('sys.stdout', new=StringIO()) as fake_output:
            random.seed(4)
            run_game()
            self.assertEqual(fake_output.getvalue().strip(), "Thanks for playing!")

if __name__ == '__main__':
    unittest.main()