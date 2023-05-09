import unittest
from io import StringIO
from unittest.mock import patch


class TestCombineNames(unittest.TestCase):
    @patch("builtins.input", side_effect=["John", "Doe"])
    def test_combine_names(self, mock_input):
        expected_output = "John Doe"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            full_name = combine_names()
            self.assertEqual(full_name, expected_output)
            self.assertEqual(fake_output.getvalue().strip(), expected_output)

    @patch("builtins.input", side_effect=["Jane", "Doe"])
    def test_combine_names_custom_input(self, mock_input):
        expected_output = "Jane Doe"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            full_name = combine_names()
            self.assertEqual(full_name, expected_output)
            self.assertEqual(fake_output.getvalue().strip(), expected_output)

    @patch("builtins.input", side_effect=["", ""])
    def test_combine_names_empty_input(self, mock_input):
        expected_output = " "
        with patch("sys.stdout", new=StringIO()) as fake_output:
            full_name = combine_names()
            self.assertEqual(full_name, expected_output)
            self.assertEqual(fake_output.getvalue().strip(), expected_output)

    @patch("builtins.input", side_effect=["John", ""])
    def test_combine_names_missing_last_name(self, mock_input):
        expected_output = "John "
        with patch("sys.stdout", new=StringIO()) as fake_output:
            full_name = combine_names()
            self.assertEqual(full_name, expected_output)
            self.assertEqual(fake_output.getvalue().strip(), expected_output)


if __name__ == "__main__":
    unittest.main()
