import unittest
from problem import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # Basic cases
    def test_case_1(self):
        """Find the longest substring without repeating characters."""
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_case_2(self):
        """Find the longest substring without repeating characters."""
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)

    def test_case_3(self):
        """Find the longest substring without repeating characters."""
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)

    # Edge cases
    def test_empty_string(self):
        """Test with an empty string."""
        self.assertEqual(self.solution.lengthOfLongestSubstring(""), 0)

    def test_single_character_string(self):
        """Test with a single character string."""
        self.assertEqual(self.solution.lengthOfLongestSubstring("a"), 1)

    def test_all_repeating_characters(self):
        """Test with all repeating characters."""
        self.assertEqual(self.solution.lengthOfLongestSubstring("aaaaa"), 1)

    def test_two_repeating_characters(self):
        """Test with two repeating characters."""
        self.assertEqual(self.solution.lengthOfLongestSubstring("abba"), 2)

    def test_three_repeating_characters(self):
        """Test with three repeating characters."""
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)

    # Complex cases
    def test_large_repeating_string(self):
        """Test with a large string of repeating characters."""
        self.assertEqual(self.solution.lengthOfLongestSubstring("a" * 100000), 1)

    def test_large_alternating_string(self):
        """Test with a large alternating string."""
        self.assertEqual(self.solution.lengthOfLongestSubstring("ab" * 50000), 2)

    def test_varied_characters(self):
        """Test with a string containing varied characters."""
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)

    # Extreme cases
    def test_large_input(self):
        """Test with a very large input string."""
        input_string = "a" * 100000
        self.assertEqual(self.solution.lengthOfLongestSubstring(input_string), 1)

if __name__ == "__main__":
    unittest.main()
