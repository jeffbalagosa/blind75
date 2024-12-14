import unittest

from problem import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assertCountEqual(self, first, second):
        # Helper method to compare lists regardless of order
        self.assertEqual(sorted(first), sorted(second))

    def test_example_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        expected = [1, 2]
        result = self.solution.topKFrequent(nums, k)
        self.assertCountEqual(result, expected)

    def test_example_2(self):
        nums = [1]
        k = 1
        expected = [1]
        result = self.solution.topKFrequent(nums, k)
        self.assertCountEqual(result, expected)

    def test_all_same_frequency(self):
        nums = [1, 2, 3, 4]
        k = 2
        # Any two numbers should be valid
        result = self.solution.topKFrequent(nums, k)
        self.assertEqual(len(result), k)
        self.assertTrue(all(x in nums for x in result))

    def test_negative_numbers(self):
        nums = [-1, -1, -2, -2, -3]
        k = 2
        expected = [-1, -2]
        result = self.solution.topKFrequent(nums, k)
        self.assertCountEqual(result, expected)

    def test_k_equals_length(self):
        nums = [1, 2, 3, 4]
        k = 4
        expected = [1, 2, 3, 4]
        result = self.solution.topKFrequent(nums, k)
        self.assertCountEqual(result, expected)

    def test_multiple_frequencies(self):
        nums = [1, 1, 1, 2, 2, 3, 3, 3, 3]
        k = 2
        expected = [3, 1]
        result = self.solution.topKFrequent(nums, k)
        self.assertCountEqual(result, expected)

    def test_large_numbers(self):
        nums = [10000, 10000, 9999, 9999, 9999, -10000]
        k = 2
        expected = [9999, 10000]
        result = self.solution.topKFrequent(nums, k)
        self.assertCountEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
