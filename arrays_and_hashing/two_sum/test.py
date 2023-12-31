import unittest

from problem import Solution


class Test(unittest.TestCase):
    def test_twoSum_case1(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_twoSum_case2(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([3, 2, 4], 6), [1, 2])

    def test_twoSum_case3(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([3, 3], 6), [0, 1])


if __name__ == "__main__":
    unittest.main()
