import unittest
from unittest.mock import patch
from io import StringIO
import random

from rps_game import play_game, run_game


class TestRPSGame(unittest.TestCase):

    # Test the play_game() function
    def test_play_game_tie(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            random.seed(1)
            play_game()
            self.assertEqual(fake_output.getvalue().strip(), "It's a tie!")

    def test_play_game_win(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            random.seed(2)
            play_game()
            self.assertEqual(fake_output.getvalue().strip(), "You win!")

    def test_play_game_loss(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            random.seed(3)
            play_game()
            self.assertEqual(fake_output.getvalue().strip(), "You lose!")

    # Test the run_game() function
    def test_run_game_once(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            random.seed(4)
            with patch('builtins.input', side_effect=['rock']):
                run_game()
                self.assertIn("You chose rock, and the computer chose paper.", fake_output.getvalue())
                self.assertIn("You lose!", fake_output.getvalue())
                self.assertIn("Do you want to play again? (yes/no): ", fake_output.getvalue())

    @patch('builtins.input', side_effect=['yes', 'rock', 'yes', 'paper', 'no'])
    def test_run_game_twice(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            random.seed(5)
            run_game()
            self.assertIn("You chose rock, and the computer chose scissors.", fake_output.getvalue())
            self.assertIn("You win!", fake_output.getvalue())
            self.assertIn("Do you want to play again? (yes/no): ", fake_output.getvalue())
            self.assertIn("You chose paper, and the computer chose scissors.", fake_output.getvalue())
            self.assertIn("You lose!", fake_output.getvalue())

    # Additional tests
    @patch('builtins.input', side_effect=['yes', 'rock', 'yes', 'paper', 'yes', 'scissors', 'no'])
    def test_run_game_three_times(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            random.seed(6)
            run_game()
            self.assertIn("You chose rock, and the computer chose paper.", fake_output.getvalue())
            self.assertIn("You lose!", fake_output.getvalue())
            self.assertIn("Do you want to play again? (yes/no): ", fake_output.getvalue())
            self.assertIn("You chose paper, and the computer chose scissors.", fake_output.getvalue())
            self.assertIn("You lose!", fake_output.getvalue())
            self.assertIn("Do you want to play again? (yes/no): ", fake_output.getvalue())
            self.assertIn("You chose scissors, and the computer chose rock.", fake_output.getvalue())
            self.assertIn("You lose!", fake_output.getvalue())

    @patch('builtins.input', side_effect=['yes', 'banana', 'yes', 'rock', 'no'])
    def test_run_game_invalid_input(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            random.seed(7)
            run_game()
            self.assertIn("Invalid input. Please choose rock, paper, or scissors.", fake_output.getvalue())
            self.assertIn("You chose rock, and the computer chose scissors.", fake_output.getvalue())
            self.assertIn("You win!", fake_output.getvalue())
            self.assertIn("Do you want to play again? (yes/no): ", fake_output.getvalue())


if __name__ == '__main__':
    unittest.main()