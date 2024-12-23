# 424. Longest Repeating Character Replacement

## Description

Given a string `s` and an integer `k`, you can replace up to `k` characters in `s` with any other uppercase English letters.

Return the length of the longest substring consisting of the same letter after performing at most `k` replacements.

---

### Example 1:

**Input:**
`s = "ABAB", k = 2`

**Output:**
`4`

**Explanation:**
Replace the two `'A'`s with `'B'`s (or the two `'B'`s with `'A'`s) to form `"BBBB"` (or `"AAAA"`).

---

### Example 2:

**Input:**
`s = "AABABBA", k = 1`

**Output:**
`4`

**Explanation:**
Replace the one `'A'` in the middle with `'B'` to form `"AABBBBA"`.
The substring `"BBBB"` has a length of 4. Other valid solutions exist.

---

### Constraints:

- `1 <= s.length <= 100,000`
- `s` consists of only uppercase English letters.
- `0 <= k <= s.length`
