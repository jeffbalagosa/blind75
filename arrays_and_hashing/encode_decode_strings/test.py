import unittest

from problem import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_encode_empty(self):
        self.assertEqual(self.solution.encode([]), "")

    def test_decode_empty(self):
        self.assertEqual(self.solution.decode(""), [])

    def test_encode_single(self):
        self.assertEqual(self.solution.encode(["a"]), "1,#a")

    def test_decode_single(self):
        self.assertEqual(self.solution.decode("1,#a"), ["a"])

    def test_encode_multiple(self):
        self.assertEqual(self.solution.encode(["a", "b"]), "1,1,#ab")

    def test_decode_multiple(self):
        self.assertEqual(self.solution.decode("1,1,#ab"), ["a", "b"])


if __name__ == "__main__":
    unittest.main()
