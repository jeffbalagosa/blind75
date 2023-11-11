import unittest

from problem import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isPalindrome(self):
        self.assertTrue(self.solution.isPalindrome("racecar"))

    def test_isPalindrome_false(self):
        self.assertFalse(self.solution.isPalindrome("hello"))

    def test_isPalindrome_empty(self):
        self.assertTrue(self.solution.isPalindrome(""))


if __name__ == "__main__":
    unittest.main()
