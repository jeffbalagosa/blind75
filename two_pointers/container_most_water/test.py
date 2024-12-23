import unittest
from problem import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertEqual(self.solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_case_2(self):
        self.assertEqual(self.solution.maxArea([1, 1]), 1)

    def test_case_3(self):
        self.assertEqual(self.solution.maxArea([4, 3, 2, 1, 4]), 16)

    def test_case_4(self):
        self.assertEqual(self.solution.maxArea([1, 2, 1]), 2)

    def test_empty_array(self):
        self.assertEqual(self.solution.maxArea([]), 0)

    def test_single_element(self):
        self.assertEqual(self.solution.maxArea([1]), 0)

    def test_same_heights(self):
        self.assertEqual(self.solution.maxArea([5, 5, 5, 5]), 15)

    def test_with_zeros(self):
        self.assertEqual(self.solution.maxArea([0, 8, 0, 0]), 0)

    def test_large_array(self):
        large_array = [i % 10 for i in range(10000)]
        self.assertGreater(self.solution.maxArea(large_array), 0)


if __name__ == "__main__":
    unittest.main()
