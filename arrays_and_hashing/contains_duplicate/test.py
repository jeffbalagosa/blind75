from problem import Solution


class TestSolution:
    def test_1(self):
        assert Solution().containsDuplicate([1, 2, 3, 1])

    def test_2(self):
        assert not Solution().containsDuplicate([1, 2, 3, 4])

    def test_3(self):
        assert Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])


if __name__ == "__main__":
    unittest.main()
