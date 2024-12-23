### Instructions: Longest Substring Without Repeating Characters

#### Problem Statement
Find the **length of the longest substring** without duplicate characters in a given string `s`.

- A **substring** is a contiguous sequence of characters within a string.

#### Examples

1. **Example 1**:
   - **Input**: `s = "zxyzxyz"`
   - **Output**: `3`
   - **Explanation**: The substring `"xyz"` is the longest substring without duplicate characters.

2. **Example 2**:
   - **Input**: `s = "xxxx"`
   - **Output**: `1`
   - **Explanation**: The substring `"x"` is the longest substring without duplicate characters.

#### Constraints
- `0 <= s.length <= 1000`
- `s` consists of printable ASCII characters.

#### Recommended Time & Space Complexity
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(m)`, where:
  - `n` is the length of the string.
  - `m` is the number of unique characters in the string.

---

### Hints

1. **Hint 1**:
   - A brute force approach would involve checking all substrings starting from each index `i` and finding the maximum length of a substring without duplicates. This can be done using a hash set to detect duplicates in `O(1)` time, but this approach is inefficient. Can you optimize it?

2. **Hint 2**:
   - Use the **sliding window technique**. This approach dynamically adjusts the window to maintain a valid substring without duplicate characters.

3. **Hint 3**:
   - Implement the sliding window approach:
     - Use two pointers, `r` (right boundary) and `l` (left boundary), to define the window.
     - Maintain a hash set to store characters currently in the window.
     - If a duplicate character is encountered at index `r`, move the `l` pointer to shrink the window until there are no duplicates.
     - Remove characters from the hash set as they are excluded from the window.
     - At each iteration, calculate the current window size as `r - l + 1` and update the result if the size exceeds the current maximum.
