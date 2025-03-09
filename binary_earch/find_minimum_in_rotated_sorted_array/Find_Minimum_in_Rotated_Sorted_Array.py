from typing import List
import unittest


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)


class TestFindMin(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_element(self):
        self.assertEqual(self.solution.findMin([5]), 5)

    def test_multiple_elements(self):
        self.assertEqual(self.solution.findMin([4, 5, 6, 7]), 4)

    def test_negative_numbers(self):
        self.assertEqual(self.solution.findMin([-3, -1, 0, 2]), -3)

    def test_unsorted_list(self):
        self.assertEqual(self.solution.findMin([3, 1, 4, 1, 5]), 1)

    def test_all_same_elements(self):
        self.assertEqual(self.solution.findMin([2, 2, 2, 2]), 2)


if __name__ == "__main__":
    unittest.main()
