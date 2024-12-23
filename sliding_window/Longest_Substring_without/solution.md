```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.

        Parameters:
        s (str): Input string

        Returns:
        int: Length of the longest substring without duplicate characters
        """
        # Dictionary to store the last seen index of each character
        last_seen = {}

        # Initialize pointers and result variable
        left = 0  # Left boundary of the sliding window
        max_length = 0  # Maximum length of substring without duplicates

        # Iterate through the string with the right pointer
        for right in range(len(s)):
            # If the character is already in the current window, update the left boundary
            if s[right] in last_seen:
                left = max(last_seen[s[right]] + 1, left)

            # Update the last seen index of the current character
            last_seen[s[right]] = right

            # Calculate the length of the current window and update the maximum length
            max_length = max(max_length, right - left + 1)

        return max_length
```
