# Solution

```Python
def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            # Skip non-alphanumeric characters
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            # Compare characters
            if s[i].lower() != s[j].lower():
                return False

            # Move pointers
            i += 1
            j -= 1

        return True
```
