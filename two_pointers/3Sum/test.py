import unittest
from problem import Solution


class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_input(self):
        self.assertEqual(self.solution.threeSum([]), [])

    def test_no_solution(self):
        self.assertEqual(self.solution.threeSum([1, 2, 3]), [])

    def test_single_solution(self):
        self.assertEqual(
            sorted(self.solution.threeSum([-1, 0, 1, 2, -1, -4])),
            sorted([[-1, -1, 2], [-1, 0, 1]]),
        )

    def test_multiple_solutions(self):
        self.assertEqual(
            sorted(self.solution.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4])),
            sorted(
                [
                    [-4, 0, 4],
                    [-4, 1, 3],
                    [-3, -1, 4],
                    [-3, 0, 3],
                    [-3, 1, 2],
                    [-2, -1, 3],
                    [-2, 0, 2],
                    [-1, -1, 2],
                    [-1, 0, 1],
                ]
            ),
        )

    def test_duplicate_numbers(self):
        self.assertEqual(self.solution.threeSum([-1, -1, -1, 0, 1, 1, 1]), [[-1, 0, 1]])


if __name__ == "__main__":
    unittest.main()
