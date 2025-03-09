from typing import List
import unittest


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertEqual(self.solution.search([], 5), -1)

    def test_single_element_found(self):
        self.assertEqual(self.solution.search([3], 3), 0)

    def test_single_element_not_found(self):
        self.assertEqual(self.solution.search([3], 4), -1)

    def test_target_at_start(self):
        self.assertEqual(self.solution.search([1, 2, 3, 4], 1), 0)

    def test_target_at_end(self):
        self.assertEqual(self.solution.search([1, 2, 3, 4], 4), 3)

    def test_target_in_middle(self):
        self.assertEqual(self.solution.search([1, 2, 3, 4], 3), 2)

    def test_target_not_found(self):
        self.assertEqual(self.solution.search([1, 2, 3, 4], 5), -1)

    def test_multiple_occurrences(self):
        self.assertEqual(self.solution.search([1, 2, 2, 3], 2), 1)


if __name__ == "__main__":
    unittest.main()
