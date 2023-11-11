import unittest
from problem import Solution


class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertFalse(self.solution.containsDuplicate([]))

    def test_single_element_list(self):
        self.assertFalse(self.solution.containsDuplicate([1]))

    def test_no_duplicates(self):
        self.assertFalse(self.solution.containsDuplicate([1, 2, 3, 4, 5]))

    def test_with_duplicates(self):
        self.assertTrue(self.solution.containsDuplicate([1, 2, 3, 2]))

    def test_with_multiple_duplicates(self):
        self.assertTrue(self.solution.containsDuplicate([1, 1, 1, 1, 1]))


if __name__ == "__main__":
    unittest.main()
