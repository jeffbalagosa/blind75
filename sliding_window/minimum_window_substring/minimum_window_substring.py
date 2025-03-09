import unittest


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        # Count characters in t
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # Track characters in current window
        window = {}
        have, need = 0, len(
            countT
        )  # 'need' is unique chars in t, 'have' is matched chars
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # If c is in t and its count matches, increment 'have'
            if c in countT and window[c] == countT[c]:
                have += 1

            # Shrink window while we have all required chars
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Shrink from left
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""


class TestMinimumWindowSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # Basic cases from the problem statement
    def test_example_1(self):
        """Test case from Example 1: s = 'ADOBECODEBANC', t = 'ABC'"""
        self.assertEqual(self.solution.minWindow("ADOBECODEBANC", "ABC"), "BANC")

    def test_example_2(self):
        """Test case from Example 2: s = 'a', t = 'a'"""
        self.assertEqual(self.solution.minWindow("a", "a"), "a")

    def test_example_3(self):
        """Test case from Example 3: s = 'a', t = 'aa'"""
        self.assertEqual(self.solution.minWindow("a", "aa"), "")

    # Edge cases
    def test_empty_s(self):
        """Test with empty s and non-empty t"""
        self.assertEqual(self.solution.minWindow("", "ABC"), "")

    def test_empty_t(self):
        """Test with non-empty s and empty t"""
        self.assertEqual(self.solution.minWindow("ABC", ""), "")

    def test_both_empty(self):
        """Test with both s and t empty"""
        self.assertEqual(self.solution.minWindow("", ""), "")

    def test_s_shorter_than_t(self):
        """Test when s is shorter than t"""
        self.assertEqual(self.solution.minWindow("AB", "ABC"), "")

    # Additional cases
    def test_duplicate_chars_in_t(self):
        """Test with duplicate characters in t"""
        self.assertEqual(self.solution.minWindow("AABBC", "AAB"), "AAB")

    def test_no_valid_window(self):
        """Test with no valid window possible"""
        self.assertEqual(self.solution.minWindow("XYZ", "ABC"), "")

    def test_entire_string_is_min_window(self):
        """Test when the entire string is the minimum window"""
        self.assertEqual(self.solution.minWindow("ABCDE", "ABCDE"), "ABCDE")

    def test_multiple_possible_windows(self):
        """Test with multiple valid windows, ensuring the smallest is returned"""
        self.assertEqual(self.solution.minWindow("ADOBECODEBANCDE", "ABC"), "BANC")

    def test_case_sensitivity(self):
        """Test with mixed case characters, expecting case-sensitive matching"""
        self.assertEqual(
            self.solution.minWindow("aDoBeCoDeBaNc", "abc"), ""
        )  # 'abc' not found due to case

    def test_large_input(self):
        """Test with a larger input to verify performance and correctness"""
        s = "a" * 10000 + "b" * 10000 + "c"
        t = "abc"
        # The minimum window will be the last 'a' followed by all remaining characters
        expected = "a" + "b" * 10000 + "c"
        self.assertEqual(self.solution.minWindow(s, t), expected)

    def test_single_char_repeated(self):
        """Test with repeated single character in s and t"""
        self.assertEqual(self.solution.minWindow("aaaaaa", "aa"), "aa")

    def test_t_longer_than_s_with_duplicates(self):
        """Test when t has more duplicates than s can satisfy"""
        self.assertEqual(self.solution.minWindow("aaa", "aaaa"), "")


if __name__ == "__main__":
    unittest.main()
