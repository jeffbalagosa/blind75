import unittest
from problem import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_productExceptSelf(self):
        self.assertEqual(self.solution.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_productExceptSelf_2(self):
        self.assertEqual(
            self.solution.productExceptSelf([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24]
        )

    def test_productExceptSelf_3(self):
        self.assertEqual(
            self.solution.productExceptSelf([1, 2, 3, 4, 5, 6]),
            [720, 360, 240, 180, 144, 120],
        )

    def test_productExceptSelf_4(self):
        self.assertEqual(
            self.solution.productExceptSelf([1, 2, 3, 4, 5, 6, 7]),
            [5040, 2520, 1680, 1260, 1008, 840, 720],
        )


if __name__ == "__main__":
    unittest.main()
