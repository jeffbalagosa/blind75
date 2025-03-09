# 76. Minimum Window Substring

## Difficulty: Hard

## Description
Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (**including duplicates**) is included in the window. If there is no such substring, return the empty string `""`.

- The test cases will be generated such that the answer is **unique**.

## Examples

### Example 1:
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

### Example 2:
```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

### Example 3:
```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window. Since the largest window of s only has one 'a', return empty string.
```

## Constraints
- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters.

## Follow Up
Could you find an algorithm that runs in `O(m + n)` time?

## Hints

### Hint 1
Use two pointers to create a window of letters in `s`, which would have all the characters from `t`.

### Hint 2
Expand the right pointer until all the characters of `t` are covered.

### Hint 3
Once all the characters are covered, move the left pointer and ensure that all the characters are still covered to minimize the subarray size.

### Hint 4
Continue expanding the right and left pointers until you reach the end of `s`.
