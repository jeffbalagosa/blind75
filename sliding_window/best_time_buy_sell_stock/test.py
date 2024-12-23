import unittest
from problem import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertEqual(self.solution.maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_case_2(self):
        self.assertEqual(self.solution.maxProfit([7, 6, 4, 3, 1]), 0)

    def test_case_3(self):
        self.assertEqual(self.solution.maxProfit([1, 2, 3, 4, 5]), 4)

    def test_case_4(self):
        self.assertEqual(self.solution.maxProfit([7, 1, 5, 3, 6, 4, 8]), 7)

    def test_empty_array(self):
        self.assertEqual(self.solution.maxProfit([]), 0)

    def test_single_element(self):
        self.assertEqual(self.solution.maxProfit([1]), 0)

    def test_same_prices(self):
        self.assertEqual(self.solution.maxProfit([5, 5, 5, 5]), 0)

    def test_with_zeros(self):
        self.assertEqual(self.solution.maxProfit([0, 8, 0, 0]), 8)

    def test_large_array(self):
        large_array = [i % 10 for i in range(10000)]
        self.assertGreater(self.solution.maxProfit(large_array), 0)


if __name__ == "__main__":
    unittest.main()
