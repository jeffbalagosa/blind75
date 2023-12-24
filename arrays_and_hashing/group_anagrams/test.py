import unittest

from problem import Solution


class Test(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        self.assertEqual(
            solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
            [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]],
        )

    def test_2(self):
        solution = Solution()
        self.assertEqual(
            solution.groupAnagrams([""]),
            [[""]],
        )

    def test_3(self):
        solution = Solution()
        self.assertEqual(
            solution.groupAnagrams(["a"]),
            [["a"]],
        )


if __name__ == "__main__":
    unittest.main()
