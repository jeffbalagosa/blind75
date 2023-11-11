import unittest
from problem import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_001(self):
        intervals = [[0, 30], [5, 10], [15, 20]]
        result = self.solution.can_attend_meetings(intervals)
        self.assertEqual(result, False)

    def test_002(self):
        intervals = [[7, 10], [2, 4]]
        result = self.solution.can_attend_meetings(intervals)
        self.assertEqual(result, True)


if __name__ == "__main__":
    unittest.main()
