import unittest
from problem import Solution


class Test(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = solution.groupAnagrams(words)
        expected = [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]
        self.assertEqual(sorted(map(sorted, result)),
                         sorted(map(sorted, expected)))

    def test_2(self):
        solution = Solution()
        result = solution.groupAnagrams([""])
        expected = [[""]]
        self.assertEqual(sorted(map(sorted, result)),
                         sorted(map(sorted, expected)))

    def test_3(self):
        solution = Solution()
        result = solution.groupAnagrams(["a"])
        expected = [["a"]]
        self.assertEqual(sorted(map(sorted, result)),
                         sorted(map(sorted, expected)))


if __name__ == "__main__":
    unittest.main()
