import unittest
from problem import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_is_anagram_positive_case(self):
        self.assertTrue(self.solution.isAnagram("anagram", "nagaram"))

    def test_is_anagram_negative_case(self):
        self.assertFalse(self.solution.isAnagram("rat", "car"))

    def test_is_anagram_empty_strings(self):
        self.assertTrue(self.solution.isAnagram("", ""))

    def test_is_anagram_single_char_negative(self):
        self.assertFalse(self.solution.isAnagram("a", "b"))

    def test_is_anagram_three_chars_positive(self):
        self.assertTrue(self.solution.isAnagram("abc", "cba"))


if __name__ == "__main__":
    unittest.main()
