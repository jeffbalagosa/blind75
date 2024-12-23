import unittest
from problem import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # Basic cases
    def test_case_1(self):
        """Replace 2 characters to maximize repeating substring."""
        self.assertEqual(self.solution.characterReplacement("ABAB", 2), 4)

    def test_case_2(self):
        """Replace 1 character to maximize repeating substring."""
        self.assertEqual(self.solution.characterReplacement("AABABBA", 1), 4)

    # Edge cases
    def test_empty_string(self):
        """Test with an empty string."""
        self.assertEqual(self.solution.characterReplacement("", 1), 0)

    def test_single_character_string(self):
        """Test with a single character string."""
        self.assertEqual(self.solution.characterReplacement("A", 1), 1)

    def test_k_zero(self):
        """Test with no replacements allowed."""
        self.assertEqual(self.solution.characterReplacement("AABA", 0), 2)
        self.assertEqual(self.solution.characterReplacement("ABCD", 0), 1)

    # Complex cases
    def test_large_repeating_string(self):
        """Test with a large string of repeating characters."""
        self.assertEqual(self.solution.characterReplacement("AAAAAA", 2), 6)

    def test_large_alternating_string(self):
        """Test with a large alternating string."""
        self.assertEqual(self.solution.characterReplacement("ABABABABABAB", 3), 7)

    def test_varied_characters(self):
        """Test with a string containing varied characters."""
        self.assertEqual(self.solution.characterReplacement("XYZABABAB", 2), 5)

    # Extreme cases
    def test_all_distinct_characters(self):
        """Test with all distinct characters."""
        self.assertEqual(self.solution.characterReplacement("ABCDEFG", 3), 4)

    def test_max_replacements(self):
        """Test when k allows replacing all characters."""
        self.assertEqual(self.solution.characterReplacement("ABCDE", 5), 5)

    def test_no_replacement_needed(self):
        """Test when no replacements are needed."""
        self.assertEqual(self.solution.characterReplacement("AAAAA", 2), 5)

    def test_large_input(self):
        """Test with a very large input string."""
        input_string = "A" * 100000
        self.assertEqual(self.solution.characterReplacement(input_string, 100), 100000)


if __name__ == "__main__":
    unittest.main()
