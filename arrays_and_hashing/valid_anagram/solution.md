# Solution

```Python
def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```

Time complexity: O(nlogn) where n is the length of s or t.
