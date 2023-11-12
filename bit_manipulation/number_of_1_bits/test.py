import unittest
from problem import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_hammingWeight(self):
        self.assertEqual(
            self.solution.hammingWeight(0b00000000000000000000000000001011), 3
        )
        self.assertEqual(
            self.solution.hammingWeight(0b00000000000000000000000010000000), 1
        )
        self.assertEqual(
            self.solution.hammingWeight(0b11111111111111111111111111111101), 31
        )

    def test_zero(self):
        self.assertEqual(self.solution.hammingWeight(0), 0)

    def test_max_int(self):
        self.assertEqual(
            self.solution.hammingWeight(0b11111111111111111111111111111111), 32
        )


if __name__ == "__main__":
    unittest.main()
