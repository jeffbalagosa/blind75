import unittest
from problem import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty(self):
        self.assertEqual(self.solution.longestConsecutive([]), 0)

    def test_single(self):
        self.assertEqual(self.solution.longestConsecutive([1]), 1)

    def test_multiple(self):
        self.assertEqual(self.solution.longestConsecutive([100, 4, 200, 1, 3, 2]), 4)

    def test_multiple2(self):
        self.assertEqual(self.solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)


if __name__ == "__main__":
    unittest.main()
