# Leetcode Problem: Encode and Decode Strings

## Difficulty: Medium

## Description
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Implement the following methods:
- `encode(strs: List[str]) -> str`: Encodes a list of strings into a single string.
- `decode(s: str) -> List[str]`: Decodes the single string back into the original list of strings.

---

## Example 1:
**Input**:
```
["neet", "code", "love", "you"]
```
**Output**:
```
["neet", "code", "love", "you"]
```

---

## Example 2:
**Input**:
```
["we", "say", ":", "yes"]
```
**Output**:
```
["we", "say", ":", "yes"]
```

---

## Constraints:
1. `0 <= strs.length < 100`
2. `0 <= strs[i].length < 200`
3. Each string `strs[i]` contains only UTF-8 characters.

---

## Recommended Time & Space Complexity
- Time complexity: `O(m)` for each `encode()` and `decode()` call, where `m` is the sum of the lengths of all the strings.
- Space complexity: `O(1)` for auxiliary space beyond the output.

---

## Hints:
### Hint 1
A naive solution would be to use a non-ASCII character as a delimiter. Can you think of a better way?

### Hint 2
Try to encode and decode the strings using a smart approach based on the lengths of each string. How can you differentiate between the lengths and any numbers that might be present in the strings?

### Hint 3
Use an encoding approach where each string is prefixed by its length, followed by a separator character (e.g., `#`), and then the string itself. To decode, read the length, skip the separator, and extract the string.
